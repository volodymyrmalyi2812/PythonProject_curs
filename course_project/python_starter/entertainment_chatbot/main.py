
from colorama import Fore, Style, init

from bot.data import CATEGORY_NAMES
from bot.entertainment import (
    english_programmer_joke,
    get_genres,
    interesting_story,
    recommend_item,
    ukrainian_joke,
)
from bot.games import play_guess_number, play_rock_paper_scissors
from bot.ui import ask_choice, display_menu, show_main_menu, show_title


def recommendations_menu(category: str) -> None:
    genres = get_genres(category)
    choices = [(str(i), genre) for i, genre in enumerate(genres, start=1)]
    choices.append(("0", "Назад"))
    print(f"\nОберіть жанр ({CATEGORY_NAMES[category]}):")
    display_menu("Жанр", choices)
    choice = ask_choice()
    if choice == "0":
        return
    if not choice.isdigit() or not 1 <= int(choice) <= len(genres):
        print("Невірний номер жанру. Спробуйте ще раз через головне меню.")
        return
    genre = genres[int(choice) - 1]
    item = recommend_item(category, genre)
    print(Fore.GREEN + f"Моя рекомендація ({genre}): {item}" + Style.RESET_ALL)


def games_menu() -> None:
    while True:
        display_menu("Мініігри", [
            ("1", "Камінь — ножиці — папір"),
            ("2", "Вгадай число"),
            ("0", "Повернутися в головне меню"),
        ])
        choice = ask_choice()
        if choice == "1":
            play_rock_paper_scissors()
        elif choice == "2":
            play_guess_number()
        elif choice == "0":
            return
        else:
            print("Невірний пункт меню.")


def main() -> None:
    init(autoreset=True)
    show_title()
    while True:
        show_main_menu()
        choice = ask_choice()
        if choice == "1":
            recommendations_menu("movies")
        elif choice == "2":
            recommendations_menu("music")
        elif choice == "3":
            recommendations_menu("video_games")
        elif choice == "4":
            print(ukrainian_joke())
        elif choice == "5":
            print(english_programmer_joke())
        elif choice == "6":
            print(interesting_story())
        elif choice == "7":
            games_menu()
        elif choice == "0":
            print("Дякуємо за гру! До зустрічі 👋")
            return
        else:
            print("Невірний вибір. Будь ласка, оберіть число з меню.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nРоботу бота завершено.")
