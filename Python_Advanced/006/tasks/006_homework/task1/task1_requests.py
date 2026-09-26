'''
Завдання 1
Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database,
використовуючи стандартну бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp.
Кроки, які мають бути залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200.
Перевірте хід виконання програми на >3 ресурсах і перегляньте послідовність запису логів в обох варіантах і порівняйте результати.
Для двох видів завдань використовуйте різні файли для логування, щоби порівняти отриманий результат
'''

import requests
import sqlite3
import asyncio
from datetime import datetime

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]


def create_db():
    connection = sqlite3.connect("requests_logs.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        time DATETIME
    )
    """)

    connection.commit()
    connection.close()


def log(message):
    connection = sqlite3.connect("requests_logs.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO logs (message, time) VALUES (?, ?)",
        (message, datetime.now())
    )

    connection.commit()
    connection.close()


async def get_page(url):
    log(f"Request started: {url}")

    response = await asyncio.to_thread(requests.get, url)

    log(f"Response received: {url}, status {response.status_code}")


async def main():
    create_db()

    tasks = []

    for url in urls:
        tasks.append(get_page(url))

    await asyncio.gather(*tasks)


asyncio.run(main())