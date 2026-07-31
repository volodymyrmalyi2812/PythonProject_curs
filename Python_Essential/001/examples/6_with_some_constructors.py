class MyClass:
    """Клас з визначенням декількох конструкторів з параметрами"""
    def __init__(self, name):
        self.name = name
        print(f"I'm Constructor 1 with argument {self.name}")

    # this will overwrite the above constructor definition
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Constructor 2 with arguments {self.name}, {self.age}')


# Constructor 1 with arguments "Test":
# TypeError: MyClass.__init__() missing 1 required positional argument: 'age'
# mc1 = MyClass("Test")

# Constructor 2 with arguments "Test", 8
mc2 = MyClass("Test", 8)
