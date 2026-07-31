'''

Завдання 1

Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

Завдання 2

Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

Завдання 3

Напишіть функцію-генератор для отримання n перших простих чисел
'''



'''

Завдання 1

Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
'''
# def reverse_gen(list):
#     for i in range(len(list) - 1, -1, -1):
#         yield list[i]
#
#
# for item in reverse_gen([10, 20, 30, 40, 50]):
#     print(item)



'''
Завдання 2

Виведіть із списку чисел список квадратів парних чисел. 
Використовуйте 2 варіанти рішення: генератор та цикл
'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def get_list(list_of_numbers):
#     for number in list_of_numbers:
#         if number % 2 == 0:
#             result = number ** 2
#         else:
#             continue
#         yield result
#
# for item in get_list(numbers):
#     print(item)
#
# result = list(get_list(numbers))
# print(result)



'''
Завдання 3

Напишіть функцію-генератор для отримання n перших простих чисел
'''


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def get_prime_numbers(numbers, n):
    count = 0

    for number in numbers:
        if number < 2:
            continue

        is_prime = True

        for divider in range(2, number):
            if number % divider == 0:
                is_prime = False
                break

        if is_prime:
            yield number
            count += 1

        if count == n:
            break

for item in get_prime_numbers(list_of_numbers, 5):
    print(item)