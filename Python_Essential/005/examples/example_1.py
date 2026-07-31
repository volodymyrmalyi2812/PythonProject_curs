# <class 'type'>
print(type(object))
# <class 'type'>
print(type(type))
# <class 'type'>
print(type(float))
# <class 'float'>
print(type(7.5))


class MyClass(object):
    pass


# <class 'type'>
print(type(MyClass))
# <class '__main__.MyClass'>
print(type(MyClass()))
# True
print(isinstance(object, object))
# True
print(isinstance(type, object))

"""Виклик type() з одним аргументом дозволяє отримати тип зазначеного[аргументом] об'єкта (зазвичай повертається той же
тип, що зберігається в атрибуті об'єкта __class__). Для перевірки відповідності типу об'єкта якому - або типу (або
декільком) рекомендується скористатися функцією isinstance(), з огляду на того що вона приймає до уваги ієрархію типів.
"""

my_var = 1.4
# <type 'float'>
print(type(my_var))

"""У версії Python 2.2 та вище виклик type() з трьома аргументами дозволяє сконструювати н
овий об'єкт типу во час виконання.
"""

# Визначення типу за допомогою інструкції
# Для Python 2 - MyType(object)


class MyType:
    x = 1.5


# Те саме визначення типу, але під час виконання за допомогою type()
MyType = type('MyType', (object,), {'x': 1.5})
print(MyType)
print(type(MyType()))
