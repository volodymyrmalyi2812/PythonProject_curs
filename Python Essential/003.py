"""

OOP. 1
Прізвище
Група
Фізика
Інформ
Історія
Визначити середній бал оцінок з фізики, кількість студентів з оцінкою 5 з інформатики та вивести відомості про них.

OOP. 2
Продавець
Найменування
Кількість
Ціна
Дата_продажу
Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити лити товар з максимальною вартістю.


OOP. 3
Найменування
Кількість
Ціна
Виробник
Дата_надходження_на_склад

Вивести відомості про товари з ціною вищою за середню.
"""
from datetime import date

"""
OOP. 2
Продавець
Найменування
Кількість
Ціна
Дата_продажу
Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити лити товар з максимальною вартістю.
"""



class Product:
    def __init__(self, seller, name, quantity, price, date_of_sale):
        self.__seller = seller
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__date_of_sale = date_of_sale

    @property
    def seller(self):
        return self.__seller
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
    def date_of_sale(self):
        return self.__date_of_sale

    def __str__(self):
        return f"{self.__seller}, {self.__name}, {self.__quantity}, {self.__price}, {self.__date_of_sale}"


first_product = Product("Bob", "Laptop", 5, 1000, date(2026, 6, 20))
second_product = Product("Ben", "PC", 3, 1500, date(2026, 5, 14))
third_product = Product("John", "Phone", 10, 800, date(2026, 3, 18))
fourth_product = Product("Іван", "Airpods", 20, 100, date(2025, 12, 10))
fifth_product = Product("Seller5", "Keyboard", 15, 200, date(2025, 10, 20))


products =  [first_product, second_product, third_product, fourth_product, fifth_product]

# Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити лити товар з максимальною вартістю.

def count_products_by_name(products, seller_name):
    count_product = 0
    product_result = []
    for product in products:
        # print(product.seller)
        if product.seller == seller_name:
            if product.seller == seller_name:
                count_product = product.quantity
                product_result = product
        else:
            continue
            print("There is no seller with this name")


    return count_product, product_result

res, total = count_products_by_name(products, "Іван1")

print(res)
print(total)
