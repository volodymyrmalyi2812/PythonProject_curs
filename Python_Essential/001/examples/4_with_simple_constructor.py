class MyClass:
    """Клас з визначенням конструктора без параметрів"""
    my_count = 0

    def __init__(self):
        print("I'm a constructor")
        MyClass.my_count += 1


# Конструктор SuperClass викликається для ініціалізації екземпляру класу
c = MyClass()
print(type(c))
print(MyClass.my_count)
