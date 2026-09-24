class MyClass:
    """__new__(cls, ...) Перший метод, який буде викликаний під час ініціалізації об'єкта. Він приймає у якості
    параметрів клас і потім будь-які інші аргументи, які будуть передані в __init__()"""
    def __new__(cls, *args, **kwargs):
        new_product = object.__new__(cls)
        print("MyClass __new__ gets called")
        return new_product

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("MyClass __init__ gets called")


product = MyClass("Test", 10)
