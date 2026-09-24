'''
Завдання 2

Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
щоб він зберігав базу посилань на диску і не «забув» при перезапуску.

За бажанням можете ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html),
який у даному випадку буде дуже зручним та спростить виконання завдання.
'''


# """
# Завдання 2
#
# Створіть програму, яка емулює роботу сервісу зі скорочення посилань.
# Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.
# """
#
# # user_full_link = input("Please enter the full link: ")
# # user_short_link = input("Please enter the short link: ")
# # my_link = {user_short_link: user_full_link}
# #
# # print(my_link)
# # print(my_link["full"])
# # print(my_link["short_link"])

import os
print("База сохраняется здесь:")
print(os.getcwd())
#для понятия сохранения списка


import shelve



with shelve.open('links') as links:
    while True:
        print('please choose one of the following options -> 1) add link, 2) find link, 3) stop')

        user_choice = input('please write your choice in numbers: ')

        if user_choice == '1':
            full_link = input('please enter the full link: ')
            short_link = input('please enter the short link: ')
            links[short_link] = full_link
            print('links was saved')

        elif user_choice == '2':
            short_link = input('please enter the short link: ')

            if short_link in links:
                print('this is your link', links[short_link])
            else:
                print('you dont have this link')

        elif user_choice == '3':
            print('you stopped the task')
            break

        else:
            print('enter valid input')