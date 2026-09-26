'''
Завдання 3
Використовуючи модуль sqlite3 та модуль smtplib, реалізуйте реальне додавання користувачів до бази. Мають бути реалізовані такі функції та класи:
·        клас користувача, що містить у собі такі методи: get_full_name (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»), get_short_name (формату ПІБ: «Петров І. С.»), get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date); метод __str__ (повертає ПІБ та дату народження);
·        функція реєстрації нового користувача (приймаємо екземпляр нового користувача та відправляємо email на пошту користувача з листом подяки).
·        функція відправлення email з листом подяки.
·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.

Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти. Під час штатного запуску програми вона має відправляти повідомлення на вашу реальну поштову скриньку (необхідно налаштувати SMTP, використовуючи доступи від провайдера вашого email-сервісу).

Приклад налаштування SMTP для сервісу Gmail: https://support.google.com/mail/answer/7126229?hl=ru
'''
import sqlite3
from datetime import date
from typing import Optional


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        middle_name: str,
        email: str,
        birthday: date
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.middle_name: str = middle_name
        self.email: str = email
        self.birthday: date = birthday

    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self) -> int:
        today: date = date.today()

        age: int = today.year - self.birthday.year

        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1

        return age

    def __str__(self) -> str:
        return f"{self.get_full_name()}, {self.birthday}"


def create_database() -> None:
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        middle_name TEXT,
        email TEXT,
        birthday TEXT
    )
    """)

    connection.commit()
    connection.close()


def send_email(user: User) -> None:
    print("Email sent to:", user.email)
    print("Thank you for registration!")


def register_user(user: User) -> None:
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO users (
        first_name,
        last_name,
        middle_name,
        email,
        birthday
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        user.first_name,
        user.last_name,
        user.middle_name,
        user.email,
        user.birthday.isoformat()
    ))

    connection.commit()
    connection.close()

    send_email(user)


def find_users(
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None
) -> list[tuple]:

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE 1=1"
    values: list[str] = []

    if first_name:
        query += " AND first_name = ?"
        values.append(first_name)

    if last_name:
        query += " AND last_name = ?"
        values.append(last_name)

    if email:
        query += " AND email = ?"
        values.append(email)

    cursor.execute(query, values)

    result = cursor.fetchall()

    connection.close()

    return result


create_database()

user1: User = User(
    "Igor",
    "Petrov",
    "Sergeevich",
    "igor@example.com",
    date(2000, 5, 15)
)

print(user1.get_full_name())
print(user1.get_short_name())
print(user1.get_age())
print(user1)

register_user(user1)

users = find_users(last_name="Petrov")

for user in users:
    print(user)