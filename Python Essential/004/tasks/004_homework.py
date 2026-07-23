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


#
# class Worker:
#     def __init__(self, name, surname, department, year_of_commencement):
#
#         if name == '':
#             raise ValueError("Name cannot be empty")
#         if surname == '':
#             raise ValueError("Surname cannot be empty")
#         if department == '':
#             raise ValueError("Department cannot be empty")
#         if year_of_commencement <= 1900 or year_of_commencement >= 2026:
#             raise ValueError("Year of commencement cannot be empty")
#
#         self.__name = name
#         self.__surname = surname
#         self.__department = department
#         self.__year_of_commencement = year_of_commencement
#
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def surname(self):
#         return self.__surname
#     @property
#     def department(self):
#         return self.__department
#     @property
#     def year_of_commencement(self):
#         return self.__year_of_commencement
#
#     def show_info(self):
#         return f"name: {self.__name}, surname: {self.__surname}, department: {self.__department}, year_of_commencement: {self.__year_of_commencement}"
#
# workers = []
#
# try:
#     amount_of_workers = int(input("Enter amount of workers: "))
#
#     for number_of_worker in range(amount_of_workers):
#         worker_surname = input("Please enter your surname: ")
#         worker_name = input("Please enter your name: ")
#         worker_department = input("Please enter your department: ")
#         worker_year_of_commencement = int(input("Please enter your year of commencement: "))
#
#         worker = Worker(
#             worker_name,
#             worker_surname,
#             worker_department,
#             worker_year_of_commencement
#         )
#
#         workers.append(worker)
#
#     user_entered_year = int(input("Please enter the year for search: "))
#     print("workers employed after year -> ", user_entered_year)
#
#     for worker in workers:
#         if worker.year_of_commencement > user_entered_year:
#             print(worker.show_info())
#
# except ValueError as error:
#     print("error", error)




'''
Завдання 4

Опишіть свій клас винятку. 
Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення, 
і перехопіть цей виняток під час виклику функції.
'''

# print(Exception.__module__)
# help(Exception)
# print(Exception.__mro__)
# проверка встроенных классов в питон

# class IncorrectValueError(Exception):
#     pass
#
# def check(value):
#     if value == 0:
#         raise IncorrectValueError ('you entered incorrect value')
#
#
# try:
#     user_value = int(input('Enter a number: '))
#     check(user_value)
#     print('the value is correct')
#
# except IncorrectValueError as error:
#     print('error', error)
#
# except ValueError:
#     print('Please enter a number')



'''
Завдання 5

Створіть програму спортивного комплексу, у якій передбачене меню: 
1 - перелік видів спорту, 2 - команда тренерів, 
3 - розклад тренувань, 4 - вартість тренування. 

Дані зберігати у словниках. 

Також передбачити пошук по прізвищу тренера, 
яке вводиться з клавіатури у відповідному пункті меню. 

Якщо ключ не буде знайдений, створити відповідний клас-Exception, 
який буде викликатися в обробнику виключень.
'''

class TrainerNotFoundError(Exception):
    pass


class SportsComplex:
    def __init__(self, list_of_sports, coaching_team, training_schedule, cost_of_training):
        self.__list_of_sports = list_of_sports
        self.__coaching_team = coaching_team
        self.__training_schedule = training_schedule
        self.__cost_of_training = cost_of_training

    @property
    def list_of_sports(self):
        return self.__list_of_sports
    @property
    def coaching_team(self):
        return self.__coaching_team
    @property
    def training_schedule(self):
        return self.__training_schedule
    @property
    def cost_of_training(self):
        return self.__cost_of_training


    def show_sports(self):
        for sport, information in self.__list_of_sports.items():
            print(sport)

    def show_trainers(self):
        for trainer, sport in self.__coaching_team.items():
            print(trainer, sport)

    def show_schedule(self):
        for sport, training_time in self.__training_schedule.items():
            print(sport, training_time)

    def show_cost_of_training(self):
        for sport, cost in self.__cost_of_training.items():
            print(sport, cost)

    def get_trainer_by_name(self, trainer_name):
        if trainer_name in self.__coaching_team:
            return self.__coaching_team[trainer_name]
        else:
            raise TrainerNotFoundError( f'{trainer_name} is not in the team')




sports = {}
trainers = {}
schedule = {}
cost = {}

try:
    amount_of_sports = int(input("Enter amount of sports: "))

    for number in range(amount_of_sports):
        print("Sport number:", number + 1)

        sport_name = input("Enter sport name: ")
        sport_information = input("Enter sport information: ")
        trainer_name = input("Enter trainer surname: ")
        training_time = input("Enter training time: ")
        training_cost = int(input("Enter training cost: "))

        sports[sport_name] = sport_information
        trainers[trainer_name] = sport_name
        schedule[sport_name] = training_time
        cost[sport_name] = training_cost


    sports_complex = SportsComplex(sports, trainers, schedule, cost)


    user_choose_action = int(input( "Please choose your action: 1 - sports, 2 - trainers, 3 - schedule, 4 - cost: "))


    if user_choose_action == 1:
        sports_complex.show_sports()

    elif user_choose_action == 2:
        sports_complex.show_trainers()

        trainer_name = input(
            "Enter trainer surname for search: "
        )

        trainer_sport = sports_complex.get_trainer_by_name(
            trainer_name
        )

        print(trainer_name, "trains", trainer_sport)

    elif user_choose_action == 3:
        sports_complex.show_schedule()

    elif user_choose_action == 4:
        sports_complex.show_cost_of_training()

    else:
        print("Please enter a valid action")


except TrainerNotFoundError as error:
    print("Error:", error)

except ValueError:
    print("Please enter a valid number")