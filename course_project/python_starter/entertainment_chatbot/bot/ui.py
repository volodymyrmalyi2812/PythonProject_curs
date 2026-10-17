
from colorama import Fore, Style
from prettytable import PrettyTable


def show_title() -> None:
    print(Fore.MAGENTA + "\n🎉 Вітаємо в розважальному чат-боті! 🎉" + Style.RESET_ALL)


def display_menu(title: str, options: list[tuple[str, str]]) -> None:
    table = PrettyTable()
    table.field_names = ["№", title]
    table.align = "l"
    for number, label in options:
        table.add_row([number, label])
    print(Fore.CYAN + str(table) + Style.RESET_ALL)


def show_main_menu() -> None:
    display_menu("Головне меню", [
        ("1", "Порадь фільм"),
        ("2", "Порадь музику"),
        ("3", "Порадь відеогру"),
        ("4", "Анекдот українською"),
        ("5", "Жарт програміста (pyjokes)"),
        ("6", "Цікава історія"),
        ("7", "Мініігри"),
        ("0", "Вихід"),
    ])


def ask_choice(prompt: str = "Ваш вибір: ") -> str:
    return input(prompt).strip()
