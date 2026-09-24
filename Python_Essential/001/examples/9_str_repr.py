class MyClass:
    """Дані методи відіграють важливу роль у створенні правильних рядкових уявлень для класу користувача."""

    def __init__(self, name, growth):
        self.name = name
        self.growth = growth

    def __str__(self):
        return f"My name is {self.name}, my height is {self.growth:.2f}"

    """Ще одне рядкове уявлення, яке використовується в об'єктах Python, відображається під час використання функції
    repr, а також при додаванні об'єктів у контейнери типу списків. За подібне відображення відповідає метод __repr__,
    він теж повинен повертати рядок, але при цьому прийнято, щоб метод повертав рядок, скопіювавши який, можна
    отримати екземпляр класу"""

    def __repr__(self):
        return f"My name is {self.name}, my height is {self.growth:.2f}"


mc1 = MyClass("Test", 172.123)
print(mc1.__str__())
mc2 = MyClass("Test", 172.123)
print(mc2.__repr__())
"""Якщо не реалізувати магічний метод __repr__ усередині класу, то при додаванні об'єктів у контейнер виведення на 
екрані буде наступним: [<__main__.MyClass object at 0x000001AF7912BEE0>, 
<__main__.MyClass object at 0x000001AF7912BDC0>]"""
my_list = [mc1, mc2]
print(my_list)
