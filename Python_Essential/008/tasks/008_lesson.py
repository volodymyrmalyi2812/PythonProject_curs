'''
OOP. 1

Прізвище

Рік народження

Посада

Зарплата

Освіта


Визначити наймолодшого працівника та надрукувати відомості про нього.

OOP. 2

Прізвище

Група

Рік народження

оцінка з фізики

оцінка з математики

оцінка з інформатики


Надрукувати прізвища студентів, які склали математику на «95», і визначити їхню кількість.

+метод принт для виводу результату зробити за допомогою итератора
+ метод для запису результатив до файлу by CBS Trainer
CBS Trainer
Translate
+ метод для запису результатив до файлу
+ метод зчитування з файлу до консоли by CBS Trainer
CBS Trainer
Translate
+ метод зчитування з файлу до консоли
has context menu
'''









'''
OOP. 1

Прізвище

Рік народження

Посада

Зарплата

Освіта

'''




class Worker:
    def __init__(self, name, year_of_birth, position, salary, experience):
        self.__name = name
        self.__year_of_birth = year_of_birth
        self.__position = position
        self.__salary = salary
        self.__experience = experience


    @property
    def name(self):
        return self.__name
    @property
    def year_of_birth(self):
        return self.__year_of_birth
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def experience(self):
        return self.__experience


    @name.setter
    def name(self, name):
        self.__name = name
    @year_of_birth.setter
    def year_of_workers(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    @position.setter
    def position(self, position):
        self.__position = position
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @experience.setter
    def experience(self, experience):
        self.__experience = experience


    def __str__(self):
        return f'name {self.__name}, year of birth {self.__year_of_birth}, position {self.__position}, salary {self.__salary}, education {self.__experience}'


first_worker = Worker('w1', 1990, 'p1', 1000, 15)
second_worker = Worker('w2', 1985, 'p2', 2900, 2)
third_worker = Worker('w3', 1991, 'p3', 2000, 10)
fourth_worker = Worker('w4', 2005, 'p4', 2500, 5)
fifth_worker = Worker('w5', 2000, 'p5', 3000, 7)

workers = [first_worker, second_worker, third_worker, fourth_worker, fifth_worker]

'''Визначити наймолодшого працівника та надрукувати відомості про нього.'''

def youngest_worker(workers):
    result = None
    youngest = 1900
    for worker in workers:
        if worker.year_of_birth > youngest:
            youngest = worker.year_of_birth
            result = worker
    return result


def print_result(result):
    youngest_worker(result)
    print(youngest_worker(result))

print_result(workers)



result = youngest_worker(workers)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(str(result))

with open("result.txt", "r", encoding="utf-8") as f:
    print("Результат из файла:")
    print(f.read())