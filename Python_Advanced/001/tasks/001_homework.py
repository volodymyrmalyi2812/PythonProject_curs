'''
Завдання 1
Ще раз розберіть усі приклади до уроку, повторіть теорію та ознайомтеся з документацією щодо розглянутих модулів.

Завдання 2
Напишіть декоратор, який буде заміряти час виконання для наданої функції.

Завдання 3

Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи для цього три наведені в тексті заняття функції — без кешу, з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10 елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.

Завдання 4

За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів.

Завдання 5

Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.

Завдання 6
Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.

Завдання 7
Створіть звичайну функцію множення двох чисел. Створіть карированну функцію множення двох чисел. Частково застосуйте її до одного аргументу, до двох аргументiв.

'''





'''
Завдання 2
Напишіть декоратор, який буде заміряти час виконання для наданої функції.
'''


import time


def execution_time(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution time:", end - start)

    return wrapper


@execution_time
def test():
    for number in range(10):
        number * 2


test()



'''
Завдання 3

Напишіть програму яка буде виводити 25 перших чисел Фібоначі, 
використовуючи для цього три наведені в тексті заняття функції — без кешу, 
з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10 елементів 
та з кешем з модулю functools з максимальною кількістю 16 елементів.

'''

from functools import cache, lru_cache

def number_without(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return (number_without(number-1) + number_without(number-2))

@cache
def number_with(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return (number_with(number-1) + number_with(number-2))

@lru_cache(maxsize=10)
def number_cache_10(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return (number_cache_10(number-1) + number_cache_10(number-2))

@lru_cache(maxsize=16)
def number_cache_16(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return (number_cache_16(number-1) + number_cache_16(number-2))

def show_fibonacci(function, title):
    print(title)

    for number in range(25):
        print(function(number))


show_fibonacci(number_without, "Fibonacci without cache:")

show_fibonacci( number_with,"Fibonacci with unlimited cache:")

show_fibonacci(number_cache_10, "Fibonacci with cache of 10 elements:")

show_fibonacci(number_cache_16,"Fibonacci with cache of 16 elements:")\



'''
'''