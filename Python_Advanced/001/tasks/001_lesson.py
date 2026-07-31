'''
OOP. 1

Назва

Кількостей

Ціна

Рік виготовлення

Виробник


Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.

OOP. 2

Назва

Частота

Об'єм оперативної пам'яті

Наявність DVD ROM

Вартість


Обчислити середню вартість усіх комп'ютерів і надрукувати найменування комп'ютерів та їхню середню вартість.

OOP. 3

Прізвище

Рік народження

Посада

Зарплата

Освіта


Визначити кількість працівників - інженерів і надрукувати всі відомості про них.

'''




'''
OOP. 1

Назва

Кількостей

Ціна

Рік виготовлення

Виробник


Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.
'''

# from functools import reduce
#
# class Product:
#     def __init__(self, name, amount, price, year_of_production, manufacturer):
#         self.__name = name
#         self.__amount = amount
#         self.__price = price
#         self.__year_of_production = year_of_production
#         self.__manufacturer = manufacturer
#
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def amount(self):
#         return self.__amount
#
#     @property
#     def price(self):
#         return self.__price
#     @property
#     def year_of_production(self):
#         return self.__year_of_production
#     @property
#     def manufacturer(self):
#         return self.__manufacturer
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @amount.setter
#     def amount(self, amount):
#         self.__amount = amount
#     @price.setter
#     def price(self, price):
#         self.__price = price
#     @year_of_production.setter
#     def year_of_production(self, year_of_production):
#         self.__year_of_production = year_of_production
#     @manufacturer.setter
#     def manufacturer(self, manufacturer):
#         self.__manufacturer = manufacturer
#
#     def __str__(self):
#         return f"{self.__name}, {self.__amount}, {self.__price}, {self.__year_of_production}, {self.__manufacturer}"
#
#
# products = [
#     Product('name1', 10, 1200, 2026, 'manufacturer1'),
#     Product('name2', 5, 1000, 2025, 'manufacturer2'),
#     Product('name3', 12, 1500, 2023, 'manufacturer3'),
#     Product('name4', 8, 2500, 2026, 'manufacturer4'),
#     Product('name5', 18, 1900, 2021, 'manufacturer5'),
# ]
#
#
# #Визначити найдорожчий товар на складі та надрукувати всі відомості про нього
#
# most_expensive_item = reduce(lambda product1, product2: product1 if product1.price > product2.price else product2, products)
#
# print(f'the most expensive item is: {most_expensive_item}')





'''
OOP. 2

Назва

Частота

Об'єм оперативної пам'яті

Наявність DVD ROM

Вартість


Обчислити середню вартість усіх комп'ютерів і надрукувати найменування комп'ютерів та їхню середню вартість.
'''

from functools import reduce

class PC:
    def __init__(self, name, frequency, ram_capacity, dvd_rom, price):
        self.__name = name
        self.__frequency = frequency
        self.__ram_capacity = ram_capacity
        self.__dvd_rom = dvd_rom
        self.__price = price

    @property
    def name(self):
        return self.__name
    @property
    def frequency(self):
        return self.__frequency
    @property
    def ram_capacity(self):
        return self.__ram_capacity
    @property
    def dvd_rom(self):
        return self.__dvd_rom
    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        self.__name = name
    @frequency.setter
    def frequency(self, frequency):
        self.__frequency = frequency
    @ram_capacity.setter
    def ram_capacity(self, ram_capacity):
        self.__ram_capacity = ram_capacity
    @dvd_rom.setter
    def dvd_rom(self, dvd_rom):
        self.__dvd_rom = dvd_rom
    @price.setter
    def price(self, price):
        self.__price = price

    def  __str__(self):
        return f'{self.__name}, {self.__frequency}, {self.__ram_capacity}, {self.__dvd_rom}, {self.__price}'


computers = [
    PC('name1', 120, 32, 'yes', 1500),
    PC('name2', 120, 16, 'no', 1000),
    PC('name3', 120, 32, 'yes', 2000),
    PC('name4', 240, 64, 'yes', 2500),
    PC('name5', 60, 8, 'no', 900),
]

#Обчислити середню вартість усіх комп'ютерів і
# надрукувати найменування комп'ютерів та їхню середню вартість.


full_price = reduce(lambda full, computer: full + computer.price, computers, 0)


avg_price = full_price / len(computers)

for computer in computers:
    print(computer.name)

print("Average price:", avg_price)



'''
OOP. 3

Прізвище

Рік народження

Посада

Зарплата

Освіта


Визначити кількість працівників - інженерів і надрукувати всі відомості про них.

'''

