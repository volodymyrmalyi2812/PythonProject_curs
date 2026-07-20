"""
Завдання 1

Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. Створіть підклас ProEditor, у якому цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. Викликайте методи перегляду та редагування документів.

Завдання 2

Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

Завдання 3

Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок вирішення методів для кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.

Завдання 4

Створіть UML-діаграми до завдань 1, 3 та 7. Збережіть їх у форматі *.uml.

Завдання 5

Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.

Завдання 6

Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів, які підрахують кількість повнолітніх людей в Україні та Америці.

Завдання 7

Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля, у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.




"""
from pyclbr import Class

"""
Завдання 1

Створіть клас Editor, який містить методи view_document та edit_document. 
Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. 
Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. 
Викликайте методи перегляду та редагування документів.
"""


# class Editor:
#     def view_document(self):
#         return "you can view your document"
#     def edit_document(self):
#         return "редагування документів недоступне для безкоштовної версії"
#
# class ProEditor(Editor):
#     def edit_document(self):
#         return "редагування документів доступне"
#
#
#
# license_key = int(input("Please enter your key: "))
#
#
#
#
# if license_key == 0:
#     user_editor = Editor()
#     print("You can use free version")
# elif license_key == 1:
#     user_editor = ProEditor()
#     print("your license key is correct ")
# else:
#     user_editor = Editor()
#     print("Please enter a valid key")
#
#
# user_editor.view_document()
# user_editor.edit_document()




"""
Завдання 2

Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. 
Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.
"""

#
# class Object:
#     def __init__(self, x_coordinate, y_coordinate):
#         self.x_coordinate = x_coordinate
#         self.y_coordinate = y_coordinate
#
# class Rectangle(Object):
#     def __init__(self, x_coordinate, y_coordinate, width, height):
#         super().__init__(x_coordinate, y_coordinate)
#         self.width = width
#         self.height = height
#
#
#
# class Clickable:
#     def click(self):
#             print("You clicked the button")
#
# class Button(Rectangle, Clickable):
#     def __init__(self, x_coordinate, y_coordinate, width, height):
#         super().__init__(x_coordinate, y_coordinate, width, height)
#
# button = Button(10, 30, 100, 100)
# rectangle = Rectangle(100, 100, 200, 200)
#
# button.click()




"""
Завдання 3

Створіть ієрархію класів із використанням множинного успадкування. 
Виведіть на екран порядок вирішення методів для кожного класу. 
Поясніть, чому лінеаризація даних класів виглядає саме так.
"""



# class First:
#     pass
# class Second(First):
#     pass
# class Third(First):
#     pass
# class Fourth(Second, Third):
#     pass
#
# print(First.mro())
# print(Second.mro())
# print(Third.mro())
# print(Fourth.mro())
#то есть в строке 140 четвертый класс наследует в начале от второго а уже потом от третьего потому что мы передали в 134 строке в скобках в начале second а уже потом third


"""
Завдання 5

Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.
"""


