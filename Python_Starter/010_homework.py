"""
Завдання 1

Ознайомитися зі специфікацією PEP 8, основними правилами та рекомендаціями з написання коду.

Завдання 2

Відкрийте файл fix_me.py із папки homework. Використовуючи звичайний текстовий редактор (Notepad), виправте всі помилки оформлення коду згідно з PEP 8.

Завдання 3

Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню. Під час створення дотримуйтесь правил специфікації PEP 8.

Завдання 4

Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу додавати у створений список на початку. Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8.
"""




"""
Завдання 2

Відкрийте файл fix_me.py із папки homework. Використовуючи звичайний текстовий редактор (Notepad), виправте всі помилки оформлення коду згідно з PEP 8.
"""


# from math import pi, e
# number = 5 #changed print to number
# count = int(input('Введите количество повторов: '))
# print(number * count)
# print(pi * number * count)
# print(e * 2)
# while number >= 0:
#     number -= 1
# user_text ='my string'
# value = 0
# for elem in user_text:
#     value += pow(user_text.find(elem), 2)
#     print("sum=", sum)
# def  mt_func(atr = 1):
#     print('atr', atr)
# print (mt_func(atr = 5))



"""
Завдання 3

Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню.
Під час створення дотримуйтесь правил специфікації PEP 8.
"""
# from math import cos, log, radians, sin, sqrt, tan
#
#
# def calculate(action, first_number, second_number):
#     if action == "addition":
#         result = first_number + second_number
#         return f"Your result is: {result}"
#
#     elif action == "subtraction":
#         result = first_number - second_number
#         return f"Your result is: {result}"
#
#     elif action == "multiplication":
#         result = first_number * second_number
#         return f"Your result is: {result}"
#
#     elif action == "division":
#         if second_number == 0:
#             return "Error: division by zero is not allowed."
#
#         result = first_number / second_number
#         return f"Your result is: {result}"
#
#     elif action == "trigonometry":
#         result_sin = sin(radians(first_number))
#         result_cos = cos(radians(first_number))
#         result_tan = tan(radians(first_number))
#
#         return (
#             f"Results for {first_number} degrees:"
#             f"sin: {result_sin}"
#             f"cos: {result_cos}"
#             f"tan: {result_tan}"
#         )
#
#     elif action == "logarithm":
#         if first_number <= 0 or second_number <= 0:
#             return "logarithm works only with positive numbers."
#
#         first_result = log(first_number)
#         second_result = log(second_number)
#
#         return (
#             f"Logarithm of the first number: {first_result}\n"
#             f"Logarithm of the second number: {second_result}"
#         )
#
#     elif action == "exponent":
#         result = first_number ** second_number
#         return f"Your result is: {result}"
#
#     elif action == "root extraction":
#         if first_number < 0 or second_number < 0:
#             return "square root cannot be calculated for negative numbers."
#
#         first_result = sqrt(first_number)
#         second_result = sqrt(second_number)
#
#         return (
#             f"Square root of the first number: {first_result}\n"
#             f"Square root of the second number: {second_result}"
#         )
#
#     return "unknown action."
#
#
#
#
# user_action = input("Please choose an action -> addition, subtraction, multiplication, division, trigonometry(sin, cos, tan), logarithm, exponent or root extraction : ").lower()
# user_first_number = float(input("Please choose the first number -> "))
# user_second_number = float(input("Please choose the second number -> "))
#
# calculate_result = calculate(user_action, user_first_number, user_second_number)
# print(calculate_result)







"""
Завдання 4

Створіть магазин канцтоварів використовуючи списки для зберігання елементів. 
Для додавання елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу додавати у створений список на початку. 
Результат вивести на екран. 
Під час створення дотримуйтесь правил специфікації PEP 8.
"""



def add_product(shop):
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))

    product = (product_name, quantity)
    shop.insert(0, product)


stationery_shop = []

product_count = int(input("How many products do you want to add? "))

for i in range(product_count):
    add_product(stationery_shop)

print("Stationery shop: ")

for product in stationery_shop:
    print(product)

