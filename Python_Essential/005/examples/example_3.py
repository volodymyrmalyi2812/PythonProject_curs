class MyClass:
    """Some text"""
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        """str"""
        return f"{self.surname}, {self.name}, {self.age}"

    @staticmethod
    def my_test():
        return 5


def test(x):
    print("My str is", x)


# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'age', 'name', 'surname']
print(dir(MyClass("Petrenko", "Dmytro", 20)))
m_c = MyClass("Petrenko", "Dmytro", 20)
print(m_c.__str__())
print(m_c.my_test())
