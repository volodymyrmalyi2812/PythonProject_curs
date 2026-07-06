'''
OOP. 1
Поля
Найменування
Кількість
Ціна
Виробник
Дата_надходження_на_склад

Визначити кількість усіх товарів, кількість яких більша за 5 і вивести відомості про ці товари.

функция повертаэ лист
класс продакт Найменування
класс конкретний продукт успадкувати вид продакт



class Computer:
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd


# ???? ???????? ???????? ???? Laptop, ?? ???? ?????? ?? ??????????? ???????? ????? ??????? ??????? super().
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model
'''

import datetime

class Product:
    def __init__(self, name):
        self.name = name


class SpecificProduct(Product):
    def __init__(self, name, amount, price, model, date_received_at_warehouse):
        super().__init__(name)

        self.amount = amount
        self.price = price
        self.model = model
        self.date_received_at_warehouse = date_received_at_warehouse

    def __str__(self):
        return f"{self.name} {self.amount} {self.price} {self.model}, {self.date_received_at_warehouse}"

first_product = SpecificProduct("macbook", 5, 1500, "Pro", datetime.datetime(2026, 6, 20))
second_product = SpecificProduct("Asus", 2, 1400, "Rog", datetime.datetime(2026, 6, 4))
third_product = SpecificProduct("Acer", 10, 1100, "Nitro", datetime.datetime(2026, 5, 29))

products = [first_product, second_product, third_product]

def find_specific_product(all_products):
    product_result = []
    for product in all_products:
        if product.amount > 5:
            product_result.append(product)

    return product_result

result = find_specific_product(products)

for product in result:
    print(f"product name: {product.name}")
    print(f" amount: {product.amount}")
    print(f" price: {product.price}")
    print(f" model: {product.model}")
    print(f" date received at warehouse: {product.date_received_at_warehouse}")

