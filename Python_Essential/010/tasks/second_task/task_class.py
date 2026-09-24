'''
Назва

Кількостей

Ціна

Рік виготовлення

Виробник


Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.
'''
import re

class Product:
    def __init__(self, name, quantity, price, year_of_production, manufacturer):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__year_of_production = year_of_production
        self.__manufacturer = manufacturer

    @property
    def name(self):
        return self.__name
    @property
    def quantity(self):
        return self.__quantity
    @property
    def price(self):
        return self.__price
    @property
    def year_of_production(self):
        return self.__year_of_production
    @property
    def manufacturer(self):
        return self.__manufacturer

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’-]{2,}", name):
            raise ValueError ('name is not valid')
        self.__name = name

    @quantity.setter
    def quantity(self, quantity):
        if not  isinstance(quantity, int) or quantity < 0:
            raise ValueError ('quantity is not valid')
        self.__quantity = quantity

    @price.setter
    def price(self, price):
        if not isinstance(price, int) or price <= 0:
            raise ValueError ('price is not valid')
        self.__price = price

    @year_of_production.setter
    def year_of_production(self, year_of_production):
        if not isinstance(year_of_production, int) or year_of_production <= 1900:
            raise ValueError ('year_of_production is not valid')
        self.__year_of_production = year_of_production

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        if not isinstance(manufacturer, str) or not re.fullmatch(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’-]{2,}", manufacturer):
            raise ValueError ('manufacturer is not valid')
        self.__manufacturer = manufacturer


    def __str__(self):
        return f'name {self.__name}, quantity {self.__quantity}, price {self.__price}, year_of_production {self.__year_of_production}, manufacturer {self.__manufacturer} '
