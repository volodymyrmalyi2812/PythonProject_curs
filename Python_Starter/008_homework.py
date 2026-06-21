"""
Завдання 1

Створіть функцію, яка відображає привітання для користувача із заданим ім'ям. Якщо ім'я не вказано, вона повинна виводити привітання для користувача з Вашим ім'ям.

Завдання 2

Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.

Завдання 3

Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання, множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів. Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми. Кожна операція має бути реалізована у вигляді окремої функції. Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.

Завдання 4

Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє арифметичне, і головного циклу, що запитує у користувача числа і обчислює їх середні значення за допомогою створеної функції.

Завдання 5

Створіть програму, яка приймає як формальні параметри зріст і вагу користувача, обчислює індекс маси тіла і в залежності від результату повертає інформаційне повідомлення (маса тіла в нормі, недостатня вага або слідкуйте за фігурою). Користувач з клавіатури вводить значення росту та маси тіла та передає ці дані у вигляді фактичних параметрів під час виклику функції. Програма працює доти, доки користувач не зупинить її комбінацією символів «off».
"""
from tty import IFLAG

"""

Завдання 1

Створіть функцію, яка відображає привітання для користувача із заданим ім'ям. Якщо ім'я не вказано, вона повинна виводити привітання для користувача з Вашим ім'ям.
"""

# def hello_user():
#     if user_name:
#         print(f"Hello {user_name}!")
#     else:
#         print(f"Hello admin!")
#
# user_name = input("enter your user name: ")
# hello_user()

"""
Завдання 2

Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.
"""


# def func1_calculate(number):
#     result = number ** 2 + 2
#     return result
#
# def func2_calculate(number):
#     result = number ** 3 + 2
#     return result
#
#
# for i in range(-10, 11):
#     number = i / 2
#     result1 = func1_calculate(number)
#     result2 = func2_calculate(number)
#     print(f"Number: {number}, Result 1: {result1}, Result 2: {result2}")



"""
Завдання 3

Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання, множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів. 
Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми. 
Кожна операція має бути реалізована у вигляді окремої функції. 
Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.
"""



def calculate_addition(number1, number2):
    return number1 + number2

def calculate_subtraction(number1, number2):
    return number1 - number2

def calculate_multiplication(number1, number2):
    return number1 * number2

def calculate_division(number1, number2):
    if number2 == 0:
        return "please enter valid number"
    else:
        return number1 / number2

def calculate_exponentiation(number1, number2):
    return number1 ** number2

def calculate_square_roots(number1):
    if number1 >= 0:
        return number1 ** 0.5
    else:
        return "please enter valid number"


def calculate_cube_roots(number1):
    if number1 < 0:
        return -(abs(number1)) ** (1 / 3)
    else:
        return number1 ** (1 / 3)



while True:
    user_action = input("enter your action -> addition, subtraction, multiplication, division, exponentiation, square_roots, cube_roots").lower()
    number1 = float(input("enter your first number: "))
    number2 = int(input("enter your second number: "))
    if user_action == "addition":
        calculated_addition = calculate_addition(number1, number2)
        print(f" addition: {calculated_addition}")
    elif user_action == "subtraction":
        calculated_subtraction = calculate_subtraction(number1, number2)
        print(f" subtraction: {calculated_subtraction}")
    elif user_action == "multiplication":
        calculated_multiplication = calculate_multiplication(number1, number2)
        print(f" multiplication: {calculated_multiplication}")
    elif user_action == "division":
        calculated_division = calculate_division(number1, number2)
        print(f" division: {calculated_division}")
    elif user_action == "exponentiation":
        calculated_exponentiation = calculate_exponentiation(number1, number2)
        print(f" exponentiation: {calculated_exponentiation}")
    elif user_action == "square_roots":
        calculated_square_roots = calculate_square_roots(number1)
        print(f" square_roots: {calculated_square_roots}")
    elif user_action == "cube_roots":
        calculated_cube_roots = calculate_cube_roots(number1)
        print(f" cube_roots: {calculated_cube_roots}")
    else:
        print("please enter valid action")

    user_stop = input("If you want to stop press 0 or anything to continue")

    if user_stop == "0":
        print("you stopped your action")
        break