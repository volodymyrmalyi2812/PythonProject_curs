"""
Завдання 1

Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень.

Завдання 2

Є два списки, які наповнюються користувачем з клавіатури. Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку та навпаки без повторень. Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.


Завдання 4

Створіть цілочисельний список, введіть кількість його елементів і самі значення. Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням.

Завдання 5

Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list. Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat кількість разів. Очистіть список int_list.

Завдання 6

Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5. Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.


"""




"""
Завдання 1 

Створіть список та введіть його значення. 
Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень. 
"""
#
# new_list = [1, 3, 5, 7, 9, 11]
#
# max_list = max(new_list)
# min_list = min(new_list)
# sum_list = sum(new_list)
# avg_list = sum_list / len(new_list)
#
# print(f" max list {max_list}, min list {min_list}, sum list {sum_list}, avg list {avg_list}")



"""
Завдання 2

Є два списки, які наповнюються користувачем з клавіатури. 
Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку та навпаки без повторень. 
Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.
"""



#
# first_list = []
# second_list = []
#
#
# for value in input("Enter your numbers for 1st list: ").split():
#     first_list.append(int(value))
# for value in input("Enter your numbers for 2nd list: ").split():
#     second_list.append(int(value))
#
# print("first list: ", first_list)
# print("second list: ", second_list)
#
#
# result = []
#
# for value in first_list:
#     if value not in second_list and value not in result:
#         result.append(value)
#
# for value in second_list:
#     if value not in first_list and value not in result:
#         result.append(value)
#
# print("1st and 2nd list together without repetitions", result)
# print("reversed result ", result[::-1])
# print("sorted result", sorted(result))
# print("sorted in descending order", sorted(result, reverse=True))







"""
Завдання 3
Простим називається число, яке ділиться націло лише на одиницю і на саме себе. 
Число 1 не вважається простим. Напишіть програму, яка знаходить усі прості числа в заданому проміжку, 
виводить їх на екран, а потім на вимогу користувача виводить їхню суму або добуток
"""


#
# user_start = int(input("Please enter your start number: "))
# user_end = int(input("Please enter your end number: "))
#
# prime_number = []
#
# for number in range(user_start, user_end + 1):
#     if number >= 2:
#         num_devisor = 0
#
#         for i in range(1, number + 1):
#             if number % i == 0:
#                 num_devisor += 1
#
#         if num_devisor == 2:
#             prime_number.append(number)
#
# print("Prime numbers are: ", prime_number)
#
#
# user_action = input("Please enter your action -> сума або добуток: ")
#
# if user_action == "сума":
#     result = 0
#
#     for number in prime_number:
#         result += number
#
#     print("Your result is:", result)
# elif user_action == "добуток":
#     result = 1
#     for number in prime_number:
#         result *= number
#     print("Your result is:", result)
#
# else:
#     print("Please enter valid action")


"""
Завдання 4

Створіть цілочисельний список, введіть кількість його елементів і самі значення. 
Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням.
"""



# new_list = []
#
# user_list = int(input("Enter  how many numbers do u need: "))
#
# for number in range(user_list):
#     user_number = int(input("Enter your number: "))
#     new_list.append(user_number)
#
# print(new_list)
#
# user_choice = input("Enter your choice -> після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням: ")
# if user_choice == "1":
#     print(new_list[::-1])
# elif user_choice == "2":
#     print(sorted(new_list))
# else:
#     print("Invalid choice")



"""
Завдання 5

Створіть список натуральних чисел int_list. 
Кожне непарне значення списку додайте до нового списку new_list. 
Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat кількість разів. 
Очистіть список int_list.
"""



# int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# repeat_list = int(input("Enter how many times we should repeat: "))
# # for i in range(repeat_list):
# for number in int_list:
#     if number % 2 != 0:
#         new_list.append(number)
#     else:
#         continue
#
# new_list *= repeat_list
# print(new_list)
#
# int_list.clear()
# print(int_list)


"""
Завдання 6

Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5. 
Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.

"""

# int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
#
# for number in int_list:
#     if number % 2 != 0:
#         new_list.append(number)
#     else:
#         continue
#
# repeat = int(input("How many times should we repeat the list? "))
# new_list *= repeat
#
# print("New list: ", new_list)
# int_list.clear()
# print("int list: ", int_list)
#
# user_number = int(input("enter your number to check if our list have it: `"))
# if user_number in new_list:
#     print("index is: ", new_list.index(user_number))
#     print("times in the list: ", new_list.count(user_number))
# else:
#     print("this number is not in the list")


