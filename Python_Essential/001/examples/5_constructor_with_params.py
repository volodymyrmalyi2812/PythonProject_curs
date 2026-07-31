class MyClass:
    """Клас з визначенням конструктора з параметрами"""
    my_count = 0

    def __init__(self, name):
        self.name = name
        print(f"I'm a constructor, instance name is {self.name}")
        MyClass.my_count += 1


# Конструктор SuperClass викликається для ініціалізації екземпляру класу
c = MyClass("Test")
print(type(c))
print(MyClass.my_count)
