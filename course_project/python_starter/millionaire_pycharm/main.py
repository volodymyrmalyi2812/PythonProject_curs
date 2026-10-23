from engine import LETTERS, PRIZES, check_answer, create_game, current_prize, guaranteed_prize, select_question, use_audience, use_fifty, use_friend
from storage import SAVE_FILE, delete_save, load_game, load_stats, record_result, save_game


def money(amount):
    return f"{amount:,}".replace(",", " ") + " грн"


def show_question(state, question):
    level = state["level"]
    print("\n" + "=" * 56)
    print(f"ПИТАННЯ {level + 1} / {len(PRIZES)} | На кону: {money(PRIZES[level])}")
    print(f"Поточний виграш: {money(current_prize(level))}")
    print("=" * 56)
    print(question["text"])
    for index, answer in enumerate(question["options"]):
        if index in state["hidden_choices"]:
            print(f"  {LETTERS[index]}. —")
        else:
            print(f"  {LETTERS[index]}. {answer}")
    print("\n1 — 50/50", " 2 — Дзвінок другу", " 3 — Допомога залу")
    print("4 — Зберегти й повернутися в меню", " 5 — Забрати гроші")
    for name, key in [("50/50", "fifty"), ("Дзвінок другу", "friend"), ("Допомога залу", "audience")]:
        if state["used_hints"][key]:
            print(f"Підказка «{name}» уже використана")


def finish_game(state, prize, wrong=False):
    record_result(state["level"], wrong, prize)
    delete_save()
    print("\n" + "★" * 20)
    print(f"Ваш підсумковий виграш: {money(prize)}")
    print(f"Правильних відповідей: {state['level']}")
    if state["level"] == len(PRIZES):
        print("ВІТАЄМО! ВИ СТАЛИ МІЛЬЙОНЕРОМ!")
    print("★" * 20)


def handle_hint(state, command):
    try:
        if command == "1":
            use_fifty(state)
            print("\n50/50: два неправильні варіанти прибрано.")
        elif command == "2":
            answer = use_friend(state)
            print(f"\nДруг відповідає: «Я думаю, що правильний варіант — {answer}, але не гарантую!»")
        elif command == "3":
            results = use_audience(state)
            print("\nГолосування залу:")
            for letter, percent in results.items():
                print(f"  {letter}: {percent:3d}% {'█' * (percent // 5)}")
    except ValueError as error:
        print(f"Помилка: {error}")


def play_game(state):
    print("\nЛаскаво просимо до гри «Хто хоче стати мільйонером?»!")
    print("Відповідай A, B, C або D. У тебе є три підказки, кожна лише один раз.")
    while state["level"] < len(PRIZES):
        question = select_question(state)
        show_question(state, question)
        try:
            command = input("\nВаш вибір: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            save_game(state)
            print("\nГру автоматично збережено.")
            return
        if command in LETTERS and len(command) == 1:
            try:
                correct = check_answer(state, command)
            except ValueError as error:
                print(f"Помилка: {error}")
                continue
            if correct:
                print(f"\n✅ Правильно! Тепер у вас {money(current_prize(state['level']))}.")
                if state["level"] in (5, 10):
                    print(f"Ви досягли незгоряної суми: {money(guaranteed_prize(state['level']))}.")
                if state["level"] == len(PRIZES):
                    finish_game(state, current_prize(state["level"]))
                    return
            else:
                correct_letter = LETTERS[question["correct"]]
                prize = guaranteed_prize(state["level"])
                print(f"\n❌ Неправильно. Правильна відповідь: {correct_letter}. {question['options'][question['correct']]}")
                finish_game(state, prize, wrong=True)
                return
        elif command in ("1", "2", "3"):
            handle_hint(state, command)
        elif command == "4":
            save_game(state)
            print("\nГру збережено. Повертаємося в головне меню.")
            return
        elif command == "5":
            prize = current_prize(state["level"])
            confirm = input(f"Забрати {money(prize)} і завершити гру? (так/ні): ").strip().lower()
            if confirm in ("так", "т", "yes", "y"):
                finish_game(state, prize)
                return
        else:
            print("Невірна команда. Введіть A, B, C, D або число від 1 до 5.")


def show_stats():
    stats = load_stats()
    print("\nСТАТИСТИКА")
    print(f"Завершених ігор: {stats['games']}")
    print(f"Перемог із мільйоном: {stats['victories']}")
    print(f"Правильних відповідей: {stats['correct']}")
    print(f"Неправильних відповідей: {stats['wrong']}")
    print(f"Загалом виграно: {money(stats['earned'])}")
    print(f"Найбільший виграш: {money(stats['best'])}")
    if stats["history"]:
        print("Останні результати:")
        for entry in reversed(stats["history"]):
            print(f"  {entry['correct']} правильних, виграш {money(entry['prize'])}")


def show_rules():
    print("\nПРАВИЛА ГРИ")
    print("15 питань: 5 легких, 5 середніх і 5 складних.")
    print("За кожну правильну відповідь сума зростає.")
    print("За неправильну відповідь ви отримуєте останню незгоряну суму.")
    print("Незгоряні суми: 5 000 грн після 5 питань і 125 000 грн після 10 питань.")
    print("Можна забрати поточний виграш до відповіді на наступне питання.")
    print("Підказки 50/50, Дзвінок другу й Допомога залу доступні по одному разу за гру.")
    print("Дзвінок другу обирає випадковий доступний варіант, тому може помилятися.")
    print("Голосування залу — змодельовані відсотки, а не реальні люди.")
    print("Максимальний виграш: 1 000 000 грн.")


def main():
    while True:
        print("\n" + "=" * 48)
        print("      ХТО ХОЧЕ СТАТИ МІЛЬЙОНЕРОМ?")
        print("=" * 48)
        print("1. Нова гра")
        print("2. Продовжити збережену гру")
        print("3. Статистика")
        print("4. Правила")
        print("0. Вихід")
        try:
            choice = input("Ваш вибір: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nДо зустрічі!")
            return
        if choice == "1":
            if SAVE_FILE.exists():
                confirm = input("Нова гра замінить попереднє збереження. Продовжити? (так/ні): ").strip().lower()
                if confirm not in ("так", "т", "yes", "y"):
                    continue
                delete_save()
            play_game(create_game())
        elif choice == "2":
            state = load_game()
            if state is None:
                print("Збережену гру не знайдено або файл пошкоджено.")
            else:
                play_game(state)
        elif choice == "3":
            show_stats()
        elif choice == "4":
            show_rules()
        elif choice == "0":
            print("Дякуємо за гру! До зустрічі!")
            return
        else:
            print("Оберіть один із пунктів меню: 0, 1, 2, 3 або 4.")


if __name__ == "__main__":
    main()
