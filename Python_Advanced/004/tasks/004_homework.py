'''
Завдання 1
Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
'''
import sqlite3

connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS finance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purpose TEXT NOT NULL,
    amount REAL NOT NULL,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()


'''
Завдання 2
Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних. 
'''
import sqlite3

connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

purpose = input("Enter purpose: ")
amount = float(input("Enter amount: "))

cursor.execute("""
INSERT INTO finance (purpose, amount)
VALUES (?, ?)
""", (purpose, amount))

connection.commit()

print("Record added")

cursor.execute("SELECT * FROM finance")

for row in cursor.fetchall():
    print(row)

connection.close()

'''
Завдання 3
Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.
'''
import sqlite3

connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS money (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purpose TEXT NOT NULL,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()

purpose = input("Enter purpose: ")
amount = float(input("Enter amount: "))
money_type = input("Enter type (expense/income): ")

cursor.execute("""
INSERT INTO money (purpose, amount, type)
VALUES (?, ?, ?)
""", (purpose, amount, money_type))

connection.commit()

cursor.execute("SELECT * FROM money")

for row in cursor.fetchall():
    print(row)

connection.close()


'''
Завдання 4
Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць. Забезпечте відповідний інтерфейс користувача.
'''
import sqlite3

connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

month = input("Enter month (01-12): ")
year = input("Enter year: ")

cursor.execute("""
SELECT SUM(amount)
FROM money
WHERE type = 'expense'
AND strftime('%m', time) = ?
AND strftime('%Y', time) = ?
""", (month, year))

expenses = cursor.fetchone()[0]

cursor.execute("""
SELECT SUM(amount)
FROM money
WHERE type = 'income'
AND strftime('%m', time) = ?
AND strftime('%Y', time) = ?
""", (month, year))

income = cursor.fetchone()[0]

if expenses is None:
    expenses = 0

if income is None:
    income = 0

print("Total expenses:", expenses)
print("Total income:", income)
print("Balance:", income - expenses)

connection.close()


'''
Завдання 5
Create an Exchange Rates To USD db using API Monobank (api.monobank.ua). Do requests via request lib, parse results, write it into db. (3 examples required)
Example:
Table - Exchange Rate To USD:

id (INT PRIMARY KEY) - 1, 2, 3, ...
currency_name (TEXT) - UAH
currency_value (REAL) - 39.5
current_date (DATETIME) - 10/22/2022 7:00 PM
'''
import sqlite3
import requests
from datetime import datetime

connection = sqlite3.connect("exchange.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_name TEXT,
    currency_value REAL,
    current_date DATETIME
)
""")

url = "https://api.monobank.ua/bank/currency"

response = requests.get(url)
data = response.json()

currencies = {
    978: "EUR",
    826: "GBP",
    985: "PLN"
}

count = 0

for item in data:
    code = item.get("currencyCodeA")
    code_b = item.get("currencyCodeB")

    if code in currencies and code_b == 980:
        name = currencies[code]

        if item.get("rateSell"):
            rate = item["rateSell"]
        else:
            rate = item.get("rateCross")

        if rate:
            value = 1 / rate

            cursor.execute("""
            INSERT INTO exchange_rates
            (currency_name, currency_value, current_date)
            VALUES (?, ?, ?)
            """, (
                name,
                value,
                datetime.now()
            ))

            count += 1

            if count == 3:
                break

connection.commit()

cursor.execute("SELECT * FROM exchange_rates")

for row in cursor.fetchall():
    print(row)

connection.close()