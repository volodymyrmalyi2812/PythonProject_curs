'''
Завдання 1

Створити функцію, яка допоможе порахувати швидкість автомобіля. Набір даних, який використовується для розрахунку:

* довжина шляху;

* тривалість шляху.

Створити 5-7 тестів використовуючи оператор assert.
'''

def calculate_speed(distance, time):
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a number")
    if not isinstance(time, (int, float)):
        raise TypeError("Time must be a number")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    if time <= 0:
        raise ValueError("Time must be greater than zero")

    return distance / time


assert calculate_speed(100, 2) == 50
assert calculate_speed(120, 2) == 60
assert calculate_speed(300, 3) == 100
assert calculate_speed(50, 2) == 25
assert calculate_speed(10, 0.5) == 20
assert calculate_speed(0, 5) == 0
assert calculate_speed(90, 1.5) == 60

print("All tests passed")