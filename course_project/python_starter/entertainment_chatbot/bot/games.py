
import random
from colorama import Fore, Style

MOVES = {"1": "Камінь", "2": "Ножиці", "3": "Папір"}


def rock_paper_scissors_result(player: str, computer: str) -> str:
    if player not in MOVES.values() or computer not in MOVES.values():
        raise ValueError("Недопустимий хід")
    if player == computer:
        return "draw"
    winning_pairs = {
        ("Камінь", "Ножиці"),
        ("Ножиці", "Папір"),
        ("Папір", "Камінь"),
    }
    return "win" if (player, computer) in winning_pairs else "lose"


def number_hint(guess: int, secret: int) -> str:
    if guess == secret:
        return "correct"
    return "higher" if guess < secret else "lower"


def play_rock_paper_scissors() -> None:
    print(Fore.CYAN + "\n=== Камінь — ножиці — папір ===" + Style.RESET_ALL)
    print("1 — Камінь | 2 — Ножиці | 3 — Папір | 0 — Назад")
    while True:
        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            return
        if choice not in MOVES:
            print("Будь ласка, введіть 1, 2, 3 або 0.")
            continue
        player = MOVES[choice]
        computer = random.choice(list(MOVES.values()))
        result = rock_paper_scissors_result(player, computer)
        print(f"Ви: {player}. Комп'ютер: {computer}.")
        messages = {"win": "Ви перемогли!", "lose": "Переміг комп'ютер!", "draw": "Нічия!"}
        print(messages[result])
        print("Зіграємо ще раз? (0 — повернутися)")


def play_guess_number() -> None:
    secret = random.randint(1, 20)
    attempts_left = 6
    print(Fore.CYAN + "\n=== Вгадай число ===" + Style.RESET_ALL)
    print("Я загадав число від 1 до 20. У вас 6 спроб. 0 — вихід.")
    while attempts_left > 0:
        answer = input(f"Спроб залишилося {attempts_left}. Ваше число: ").strip()
        if answer == "0":
            print("Повернення до меню ігор.")
            return
        if not answer.isdigit() or not 1 <= int(answer) <= 20:
            print("Введіть ціле число від 1 до 20 або 0 для виходу.")
            continue
        guess = int(answer)
        hint = number_hint(guess, secret)
        if hint == "correct":
            print(Fore.GREEN + f"Вітаю! Ви вгадали число {secret}!" + Style.RESET_ALL)
            return
        attempts_left -= 1
        print("Загадане число більше." if hint == "higher" else "Загадане число менше.")
    print(f"Спроби закінчилися. Загадане число: {secret}.")
