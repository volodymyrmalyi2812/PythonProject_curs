"""
Завдання 1

Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

Завдання 2

Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).

Завдання 3

Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.

Завдання 4

Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.

Завдання 5

Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами. В результаті повинно з’явитися зображення. Перегляньте їх.
"""



"""
Завдання 1

Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? 
Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
"""


# class Car:
#     def __init__(self, make, model, year, engine, color):
#         self.__make = make
#         self.__model = model
#         self.__year = year
#         self.__engine = engine
#         self.__color = color
#
#     @property
#     def make(self):
#         return self.__make
#
#     @property
#     def model(self):
#         return self.__model
#
#     @property
#     def year(self):
#         return self.__year
#
#     @property
#     def engine(self):
#         return self.__engine
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, new_color):
#         self.__color = new_color
#
#     def __str__(self):
#         return (f"make: {self.__make}, "
#                 f"model: {self.__model}, "
#                 f"year: {self.__year}, "
#                 f"engine: {self.__engine}, "
#                 f"color: {self.__color}")
#
#
# car1 = Car("Ford", "Mustang", "2015", "Ford", "Blue")
# print(car1)
# print(car1.color)
#
# car1.color = "Black"
# print(car1)


"""
Завдання 2

Створіть 2 класи мови, наприклад, англійська та іспанська. 
В обох класів має бути метод greeting(). 
Обидва створюють різні привітання. 
Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).
"""


# class English:
#     def __init__(self, name):
#         self.__name = name
#
#     def greeting(self):
#         return "Hello from " + self.__name
#
#
# class Spanish:
#     def __init__(self, name):
#         self.__name = name
#
#     def greeting(self):
#         return "Hola desde " + self.__name
#
#
#
# def hello_friend(language1, language2):
#     print(language1.greeting())
#     print(language2.greeting())
#
# english = English("Friend1")
# spanish = Spanish("Friend2")
# hello_friend(english, spanish)



"""
Завдання 3

Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. 
Ознайомтеся з декоратором property у Python. 
Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, 
причому дані можуть бути задані в одній шкалі, а отримані в іншій.
"""

# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius
#
#     @property
#     def celsius(self):
#         return self.__celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         self.__celsius = value
#
#     @property
#     def fahrenheit(self):
#         return self.__celsius *9 / 5 + 32
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.__celsius = (value - 32) * 5 / 9
#
#
# temperature = Temperature(celsius=10)
# print(temperature.celsius)
# print(temperature.fahrenheit)



"""
Завдання 4

Опишіть два класи Base та його спадкоємця Child з методами method(), 
який виводить на консоль фрази відповідно "Hello from Base" та "Hello from Child", 
using classmethod (@classmethod) decorator.

"""

# class Base:
#     @classmethod
#     def method(cls):
#         print("Hello from Base")
#
# class Child(Base):
#     @classmethod
#     def method(cls):
#         print("Hello from Child")
# Base.method()
# Child.method()


"""
Завдання 5

Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. 
Перевизначте їх методи. 
Створіть екземпляри відповідних класів за скористайтеся всіма методами. 
В результаті повинно з’явитися зображення. Перегляньте їх.
"""

from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        self.back_color = (155, 213, 117, 255)

        # Створюємо зображення 500 × 500
        self.im = Image.new("RGBA", (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new("RGBA", (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        self.im.save("picture.png")


class Cone(Shape):
    def draw(self):
        self.draw1.polygon(
            [(250, 80), (150, 300), (350, 300)],
            fill="orange",
            outline="white"
        )

        self.draw1.ellipse(
            (150, 270, 350, 330),
            fill="orange",
            outline="white"
        )

    def erase(self):
        self.draw1.rectangle(
            (140, 70, 360, 340),
            fill=self.back_color
        )

    def save(self):
        print("Image with cone was created")
        self.im.save("draw-cone.png")
        self.im.show()


class Paraboloid(Shape):
    def draw(self):
        self.draw1.pieslice(
            (140, 100, 360, 400),
            start=0,
            end=180,
            fill="purple",
            outline="white"
        )

        # Верхня овальна частина
        self.draw1.ellipse(
            (140, 80, 360, 150),
            fill="violet",
            outline="white"
        )

    def erase(self):
        self.draw1.rectangle(
            (130, 70, 370, 410),
            fill=self.back_color
        )

    def save(self):
        print("Image with paraboloid was created")
        self.im.save("draw-paraboloid.png")
        self.im.show()


def work_with_obj(obj):
    obj.draw()
    obj.save()


cone = Cone()
work_with_obj(cone)

paraboloid = Paraboloid()
work_with_obj(paraboloid)