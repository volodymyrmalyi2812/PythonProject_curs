"""
Клас Rectangle є суперкласом, а Square є підкласом, оскільки методи Square успадковуються від Rectangle,
ми можемо викликати метод __init__() суперкласу (Rectangle.__ init__()) з класу Square використовуючи функцію super().
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        # Для квадрата просто потрібно передати один параметр length.
        # При виклику 'super().__init__()' встановимо атрибути 'length' та 'width'.
        super().__init__(length, length)


# Клас Square явно не реалізує метод area() і використовуватиме його із суперкласу Rectangle:
sqr = Square(4)
print("Area of Square is:", sqr.area())

rect = Rectangle(2, 4)
print("Area of Rectangle is:", rect.area())
