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
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Час виконання: {end - start:.6f} сек.")
        return result

    return wrapper


@timer
def test():
    return sum(range(1000000))


print(test())

'''
Завдання 3

Напишіть програму яка буде виводити 25 перших чисел Фібоначі, 
використовуючи для цього три наведені в тексті заняття функції — без кешу, 
з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10 елементів 
та з кешем з модулю functools з максимальною кількістю 16 елементів.

'''

from functools import lru_cache


def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


cache = {}


def fibonacci2(n):
    if n in cache:
        return cache[n]

    if n < 2:
        return n

    cache[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return cache[n]


@lru_cache(maxsize=10)
def fibonacci3(n):
    if n < 2:
        return n
    return fibonacci3(n - 1) + fibonacci3(n - 2)


@lru_cache(maxsize=16)
def fibonacci4(n):
    if n < 2:
        return n
    return fibonacci4(n - 1) + fibonacci4(n - 2)

print("Без кешу:")
print([fibonacci1(i) for i in range(25)])

print("Кеш довільної довжини:")
print([fibonacci2(i) for i in range(25)])

print("Кеш на 10 елементів:")
print([fibonacci3(i) for i in range(25)])

print("Кеш на 16 елементів:")
print([fibonacci4(i) for i in range(25)])



'''
Завдання 4

За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів.
'''
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Час виконання: {end - start:.6f} сек.")
        return result

    return wrapper


@timer
def test_fibonacci(func):
    return [func(i) for i in range(25)]


cache.clear()
fibonacci3.cache_clear()
fibonacci4.cache_clear()


print("Без кешу:")
test_fibonacci(fibonacci1)

print("Кеш довільної довжини:")
test_fibonacci(fibonacci2)

print("Кеш на 10 елементів:")
test_fibonacci(fibonacci3)

print("Кеш на 16 елементів:")
test_fibonacci(fibonacci4)


'''
Завдання 5

Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 != 0, numbers)
))

print(result)


'''
Завдання 6
Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.
'''
from functools import wraps


def only_even(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return filter(
            lambda x: x % 2 == 0,
            func(*args, **kwargs)
        )

    return wrapper


@only_even
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(25)))

'''
Завдання 7
Створіть звичайну функцію множення двох чисел. Створіть карированну функцію множення двох чисел. Частково застосуйте її до одного аргументу, до двох аргументiв.
'''
from functools import partial


def multiply(a, b):
    return a * b


def curried_multiply(a):
    def inner(b):
        return a * b

    return inner


print(multiply(5, 3))

print(curried_multiply(5)(3))

multiply_by_5 = partial(multiply, 5)

print(multiply_by_5(3))

multiply_5_by_3 = partial(multiply, 5, 3)

print(multiply_5_by_3())