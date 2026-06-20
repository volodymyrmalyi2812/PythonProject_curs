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


class Computer:
    def __init__(self, name, amount, price, model, date_received_at_warehouse):
        self.name = name
        self.amount = amount
        self.price = price
        self.model = model
        self.date_received_at_warehouse = date_received_at_warehouse


class Count_computers(Computer):
    def __init__(self, name, amount, price, model, date_received_at_warehouse):
        super().__init__(name, amount, price, model, date_received_at_warehouse)

        if amount > 5:
            return self