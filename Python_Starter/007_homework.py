"""
Завдання 1

Дано два рядки. Виведіть на екран символи, які є в обох рядках.
"""


# first_set = {1, 2, 3}
# second_set = {4, 5, 6}
#
# result_set = first_set.union(second_set)
# print(result_set)




"""
Завдання 2

Створіть програму, яка емулює роботу сервісу зі скорочення посилань. 
Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.
"""

# user_full_link = input("Please enter the full link: ")
# user_short_link = input("Please enter the short link: ")
# my_link = {user_short_link: user_full_link}
#
# print(my_link)
# print(my_link["full"])
# print(my_link["short_link"])



"""
Завдання 3

Створіть програму, яка має 2 списки цілочисельних значень та друкує список унікальних значень без повтору, які є в 1 списку (немає в другому) і навпаки.

Завдання
"""

# first_set = {1, 2, 3, 4, 5 }
# second_set = {3, 4, 5, 6, 7, 8}
#
# first_second = first_set - second_set
# second_first = second_set - first_set
#
# print("difference between first and second: ", first_second)
# print("difference between second and first: ", second_first)
#
# full_difference = list(first_set ^ second_set )
# print("full difference: ", full_difference)




"""
Завдання 4

Ознайомтеся за допомогою документації з класами OrderedDict, defaultdict та ChainMap модуля collections.
"""

# OrderedDict  сохраняет порядок добавления элементов
# defaultdict   автоматически создаёт значение по умолчанию, если ключ отсутствует
# ChainMap      объединяет несколько словарей в одну логическую структуру без их копирования


"""
Завдання 5

Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами та значеннями - кількістю повторів кожного слова у послідовності.
"""

# user_string = ['dog', 'cat', 'bird', 'cat', 'fish', 'mouse']
#
# user_string_to_set = {}
#
# for animal in user_string:
#     if animal in user_string_to_set:
#         user_string_to_set[animal] += 1
#     else:
#         user_string_to_set[animal] = 1
# print(user_string_to_set)


"""
Завдання 6

Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор: твір. 
Передбачте можливість виведення на екран сортування за автором та твором.
"""


# library = {"author1": "book1",
#            "author2": "book2",
#            "author3": "book3",
#            }
#
# user_author = input("Enter your author name : ")
# user_book = input("Enter your book1 name : ")
#
# library[user_author] = user_book
#
# sorted_library = sorted(library.items())
# print("Authors: ", sorted_library)
#
# sorted_book = sorted(library.values())
# print("Books: ", sorted_book)



# не уверен как отсортировать книги чтобы рядом с ними был автор





"""
Завдання 7

Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до структури(реалізуйте інтерфейс(меню), 
за допомогою якого можна робити маніпуляції з даними):

прізвище:

    посада: ...

    досвід роботи: …

    портфоліо: …

    коефіцієнт ефективності: …

    стек технологій: …

    зарплата: …

Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.
"""


employees = {
    "Lastname_1": {
        "position": "Position_1",
        "experience": 3,
        "portfolio": "Portfolio_1",
        "efficiency": 8.5,
        "technology_stack": ["Python", "Django"],
        "salary": 100000
    },

    "Lastname_2": {
        "position": "Position_2",
        "experience": 5,
        "portfolio": "Portfolio_2",
        "efficiency": 9.2,
        "technology_stack": ["JavaScript"],
        "salary": 110000
    }
}



while True:
    print("1 — show employees")
    print("2 — add or change employee   ")
    print("3 — sort for lastname")
    print("4 — show efficiency ")
    print("0 — out")

    choice = input("choose action: ")

    if choice == "1":
        for lastname in employees:
            print("lastname:", lastname)
            print("posotion:", employees[lastname]["position"])
            print("experience:", employees[lastname]["experience"])
            print("portfolio:", employees[lastname]["portfolio"])
            print("efficiency:", employees[lastname]["efficiency"])
            print("technology_stack:", employees[lastname]["technology_stack"])
            print("salary:", employees[lastname]["salary"])

    elif choice == "2":

        lastname = input("Enter lastname: ")
        position = input("Enter position: ")
        experience = int(input("Enter experience: "))
        portfolio = input("Enter portfolio: ")
        efficiency = float(input("Enter efficiency: "))
        technology_stack = input("Enter technology_stack: ").split(",")

        salary = int(input("Enter salary: "))

        employees[lastname] = {
            "position": position,
            "experience": experience,
            "portfolio": portfolio,
            "efficiency": efficiency,
            "technology_stack": technology_stack,
            "salary": salary}

    elif choice == "3":
        sorted_lastnames = sorted(employees)
        for lastname in sorted_lastnames:
            print(lastname, "—", employees[lastname]["position"])

    elif choice == "4":
        best_employee = ""
        best_efficiency = 0
        for lastname in employees:
            current_efficiency = employees[lastname]["efficiency"]
            if current_efficiency > best_efficiency:
                best_efficiency = current_efficiency
                best_employee = lastname
        print("The most effective employee:", best_employee)
        print("efficiency:", best_efficiency)

    elif choice == "0":
        print("the programme was suspended")
        break

    else:
        print("Enter valid action")
