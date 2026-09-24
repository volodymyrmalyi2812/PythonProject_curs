"""
Завдання: Облік співробітників компанії (складне)!
Створіть програму на Python для роботи зі співробітниками компанії.
Умови:
Створіть базовий клас Employee (Співробітник), який має:
приватні поля:
ім'я (__name)
зарплата (__salary)
стаж роботи (__years)
методи:
отримання даних (get-методи)
зміни зарплати (set-метод із перевіркою, що зарплата > 0)
Створіть похідний клас Manager (Менеджер), який успадковує клас Employee та має додаткове поле:
відділ (department)
Реалізуйте метод у базовому або похідному класі:
increase_salary(), який:
якщо стаж ≥ 10 років → підвищує зарплату на 20%
якщо стаж ≥ 5 років → підвищує зарплату на 10%
якщо стаж < 5 років → зарплата не змінюється
Створіть список співробітників (мінімум 6–8 об'єктів різних типів).
Розділіть співробітників на три окремі масиви:
Перший масив — співробітники зі стажем ≥ 10 років (підвищення 20%)
Другий масив — співробітники зі стажем ≥ 5 років (підвищення 10%)
Третій масив — співробітники зі стажем < 5 років (без підвищення)
Для кожного співробітника:
викличте метод підвищення зарплати
додайте його у відповідний масив
Виведіть:
усі три масиви окремо
для кожного співробітника: ім'я, стаж, нову зарплату
Додатково
Обробіть помилки через try/except (наприклад, неправильний ввід зарплати)
Додайте метод __str__() для гарного виводу інформації про співробітника




---------------------
Легка задача))
Прізвище
Вік
Кількість ігор
Кількість пропущених шайб

Визначити середній вік хокеїстів і вивести відомості про хокеїстів, вік яких понад 25 років.


"""





"""

Легка задача))
Прізвище
Вік
Кількість ігор
Кількість пропущених шайб

Визначити середній вік хокеїстів і вивести відомості про хокеїстів, вік яких понад 25 років.
"""




# class HockeyPlayer:
#     def __init__(self, name, years, number_of_games, number_of_goals_allowed):
#         self.__name = name
#         self.__years = years
#         self.__number_of_games = number_of_games
#         self.__number_of_goals_allowed = number_of_goals_allowed
#
#     def get_name(self):
#         return self.__name
#     def get_years(self):
#         return self.__years
#     def get_number_of_games(self):
#         return self.__number_of_games
#     def get_number_of_goals_allowed(self):
#         return self.__number_of_goals_allowed
#
#
#     def __str__(self):
#         return f'{self.__name}, {self.__years}, {self.__number_of_games}, {self.__number_of_goals_allowed}'
#
# player1 = HockeyPlayer("Player1", 18, 5, 3)
# player2 = HockeyPlayer("Player2", 20, 10, 15)
# player3 = HockeyPlayer("Player3", 25, 28, 7)
# player4 = HockeyPlayer("Player4", 30, 10, 15)
#
# players = [player1, player2, player3, player4]
#
# def get_avg_age(players):
#     total_age = 0
#     for player in players:
#         total_age += player.get_years()
#     return total_age / len(players)
#
# def show_players_older_than_25(players):
#     result = []
#     for player in players:
#         if player.get_years() > 25:
#             result.append(player)
#     return result
#
#
# avg_years = get_avg_age(players)
# print(f"avg years is {avg_years}")
#
# older_than_25 = show_players_older_than_25(players)
# for player in older_than_25:
#     print(player)






"""
Завдання: Облік співробітників компанії (складне)!
Створіть програму на Python для роботи зі співробітниками компанії.
Умови:
Створіть базовий клас Employee (Співробітник), який має:
приватні поля:
ім'я (__name)
зарплата (__salary)
стаж роботи (__years)
методи:
отримання даних (get-методи)
зміни зарплати (set-метод із перевіркою, що зарплата > 0)
Створіть похідний клас Manager (Менеджер), який успадковує клас Employee та має додаткове поле:
відділ (department)
Реалізуйте метод у базовому або похідному класі:
increase_salary(), який:
якщо стаж ≥ 10 років → підвищує зарплату на 20%
якщо стаж ≥ 5 років → підвищує зарплату на 10%
якщо стаж < 5 років → зарплата не змінюється
Створіть список співробітників (мінімум 6–8 об'єктів різних типів).
Розділіть співробітників на три окремі масиви:
Перший масив — співробітники зі стажем ≥ 10 років (підвищення 20%)
Другий масив — співробітники зі стажем ≥ 5 років (підвищення 10%)
Третій масив — співробітники зі стажем < 5 років (без підвищення)
Для кожного співробітника:
викличте метод підвищення зарплати
додайте його у відповідний масив
Виведіть:
усі три масиви окремо
для кожного співробітника: ім'я, стаж, нову зарплату
Додатково
Обробіть помилки через try/except (наприклад, неправильний ввід зарплати)
Додайте метод __str__() для гарного виводу інформації про співробітника

"""





class Employee:
    def __init__(self, name, salary, years):
        self.__name = name
        self.__salary = salary
        self.__years = years

    @property
    def get_name(self):
        return self.__name

    @property
    def get_salary(self):
        return self.__salary

    @property
    def get_years(self):
        return self.__years

    def set_salary(self, new_salary):
        try:
            if new_salary > 0:
                self.__salary = new_salary
            else:
                print("salary cannot be negative")
        except TypeError:
            print("salary cannot be string its number")


    def increase_salary(self):
        if self.__years >= 10:
            self.__salary = self.__salary * 1.2
        elif self.__years >= 5:
            self.__salary = self.__salary * 1.1
        else:
            self.__salary = self.__salary

    def __str__(self):
        return f"{self.__name}, {self.__salary}, {self.__years}"


class Manager(Employee):
    def __init__(self, name, salary, years, department):
        super().__init__(name, salary, years)
        self.department = department

    def __str__(self):
        return f"{self.get_name}, {self.get_salary}, {self.get_years}, {self.department}"



employees = [
    Employee("Employee1", 2000, 5),
    Employee("Employee2", 3000, 12),
    Employee("Employee3", 6000, 25),
    Manager("Manager1", 1500, 3, "Department1"),
    Manager("Manager2", 2000, 5, "Department2"),
    Manager("Manager3", 3000, 12, "Department3")
]


more_than_10years = []
more_than_5years = []
less_than_5years = []

for employee in employees:
    employee.increase_salary()

    if employee.get_years >= 10:
        more_than_10years.append(employee)
    elif employee.get_years >= 5:
        more_than_5years.append(employee)
    else:
        less_than_5years.append(employee)


for employee in more_than_10years:
    print(f"employees more than 10 years {employee}")
for employee in more_than_5years:
    print(f"employees more than 5 years {employee}")
for employee in less_than_5years:
    print(f"employees less than 5 years {employee}")


