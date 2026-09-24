'''
Прізвище

Рік народження

Посада

Зарплата

Освіта


Визначити кількість працівників, старших за 60 років, і надрукувати всі відомості про них.
'''

import re

class Worker:
    def __init__(self, name, year_of_birth, position, salary, education):
        self.__name = name
        self.__year_of_birth = year_of_birth
        self.__position = position
        self.__salary = salary
        self.__education = education

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
    def education(self):
        return self.__education

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’-]{2,}", name):
            raise ValueError ('name is not valid')
        self.__name = name

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        if not isinstance(year_of_birth, int) or year_of_birth < 1900 or year_of_birth > 2026:
            raise ValueError ('year_of_birth is not valid')
        self.__year_of_birth = year_of_birth

    @position.setter
    def position(self, position):
        if not isinstance(position, str) or not re.fullmatch(r"[A-Za-zА-Яа-яІіЇїЄєҐґ -]{2,}", position):
            raise ValueError ('position is not valid')
        self.__position = position

    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError ('salary is not valid')
        self.__salary = salary

    @education.setter
    def education(self, education):
        if not isinstance(education, str) or not re.fullmatch(r"[A-Za-zА-Яа-яІіЇїЄєҐґ -]{2,}", education):
            raise ValueError ('education is not valid')
        self.__education = education



    def __str__(self):
        return f'name {self.__name}, year of birth, {self.__year_of_birth}, position, {self.__position}, salary {self.__salary}, education {self.__education}'


