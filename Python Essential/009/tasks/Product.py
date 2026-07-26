'''
: OOP. 3

Кількість

Ціна

Рік виготовлення

Виробник


Визначити товар, кількість якого найбільше на складі, і надрукувати всі відомості про нього.
 + метод прин через итератор
 плюс метод для запису результата у файл
 плюс метод для зчитування результату з файла
 за замовчуванням инкапсуляция
'''


class Product:
    def __init__(self, name, price, year_of_production, manufacturer, in_stock):
        self.__name = name
        self.__price = price
        self.__year_of_production = year_of_production
        self.__manufacturer = manufacturer
        self.__in_stock = in_stock

    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def year_of_production(self):
        return self.__year_of_production
    @property
    def manufacturer(self):
        return self.__manufacturer
    @property
    def in_stock(self):
        return self.__in_stock

    @name.setter
    def name(self, name):
        self.__name = name
    @price.setter
    def price(self, price):
        self.__price = price
    @year_of_production.setter
    def year_of_production(self, year_of_production):
        self.__year_of_production = year_of_production
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    @in_stock.setter
    def in_stock(self, in_stock):
        self.__in_stock = in_stock

    def __str__(self):
        return f'name: {self.__name}, price: {self.__price}, year of production: {self.__year_of_production}, manufacturer: {self.__manufacturer}, in stock: {self.__in_stock}'
