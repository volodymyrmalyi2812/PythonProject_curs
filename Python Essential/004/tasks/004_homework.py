'''

Завдання 1

Вивчіть основні стандартні винятки, які перераховані в цьому уроці.

Завдання 2

Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення та піднесення до ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.

Завдання 3

Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи. Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.

Завдання 4

Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення, і перехопіть цей виняток під час виклику функції.

Завдання 5

Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню. Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
'''




'''
Завдання 2

Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення та піднесення до ступеня. 
Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.
'''


# def addition(first, second):
#     return first + second
#
# def subtraction(first, second):
#     return first - second
#
# def multiplication(first, second):
#     return first * second
#
# def division(first, second):
#     return first / second
#
# def exponentiation(first, second):
#     return first ** second
#
#
#
# while True:
#     try:
#         user_first_number = float(input("please enter your first number: "))
#         user_second_number = float(input("please enter your second number: "))
#         user_operation = input("please enter your operation --> choose between addition, subtraction, multiplication, devision, exponentiation: ").lower()
#
#         if user_operation == "addition":
#             print(addition(user_first_number, user_second_number))
#         elif user_operation == "subtraction":
#             print(subtraction(user_first_number, user_second_number))
#         elif user_operation == "multiplication":
#             print(multiplication(user_first_number, user_second_number))
#         elif user_operation == "devision":
#             print(division(user_first_number, user_second_number))
#         elif user_operation == "exponentiation":
#             print(exponentiation(user_first_number, user_second_number))
#         else:
#             print("Please enter valid operation")
#
#     except ValueError:
#         print("please enter valid numbers")
#     except ZeroDivisionError:
#         print("You cannot divide by zero or raise to a negative number")




"""
Завдання 3

Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи. 
Конструктор має генерувати виняток, якщо вказано неправильні дані. 
Введіть список працівників із клавіатури. 
Виведіть усіх співробітників, які були прийняті після цього року.
"""

from datetime import date

class Worker:
    def __init__(self, name, surname, department, year_of_commencement):
        self.__name = name
        self.__surname = surname
        self.__department = department
        self.__year_of_commencement = year_of_commencement

    @property
    def name(self):
        return self.__name
    @property
    def surname(self):
        return self.__surname
    @property
    def department(self):
        return self.__department
    @property
    def year_of_commencement(self):
        return self.__year_of_commencement

    def show_info(self):
        return f"name: {self.__name}, surname: {self.__surname}, department: {self.__department}, year_of_commencement: {self.__year_of_commencement}"

workers = []

try:
    worker_surname = input("Please enter your surname: ")
    worker_name = input("Please enter your name: ")
    worker_department = input("Please enter your department: ")
    worker_year_of_commencement = int(input("Please enter your year of commencement: "))