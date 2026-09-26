'''
Завдання 2
Взяти функцію розрахунку маси тіла з Python Starter українською/Домашнє_завдання 8/Завдання 5. Покрити її 10 тестами, щоб перевірити роботоздатність, використовуючи заздалегідь валідні дані та навпаки(введення текстових даних у поля, від'ємні значення тощо).
За необхідності взяти її та доопрацювати до максимально стабільного варіанту.
В процессі тестування використати:

- оператор assert;
- pytest;
-unittest.
'''

def calculate_bmi(weight, height):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if height <= 0:
        raise ValueError("Height must be greater than zero")

    return weight / (height ** 2)