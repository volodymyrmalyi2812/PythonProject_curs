class MetaPerson(type):
    def __repr__(cls):
        return "Person"

    def __new__(meta_person, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # повторно використовуємо метод type.__new__, це базове ООП, у ньому немає нічого чарівного
        return type.__new__(meta_person, future_class_name,
                            future_class_parents, uppercase_attr)


"""
Процес створення класу можна налаштувати, передавши ключовий аргумент metaclass у рядку визначення класу або
наслідувавши від існуючого класу, який включав такий аргумент. Клас Person та UpdatePerson є екземплярами MetaPerson
Будь-які інші ключові аргументи, зазначені у визначенні класу, передаються у всі операції metaclass, описані нижче.
"""


class Person(metaclass=MetaPerson):
    count = 0

    def __init__(self, surname, name, age, friends=[]):
        self.surname = surname
        self.name = name
        self.age = age
        self.friends = friends

    def get_friends(self):
        return self.friends


class UpdatePerson(Person):
    pass


p = Person("Dmytrenko", "Dmytro", 18, ["Ivanenko", "Petrenko"])
# Person
print(type(p))
# ім'я Person є екземпляром метакласу MetaPerson <class '__main__.MetaPerson'>
print(type(Person))
# <class 'function'>
print(type(getattr(Person, 'GET_FRIENDS')))
# True
print(isinstance(p, Person))
# Person
print(p.__class__)
# {'surname': 'Dmytrenko', 'name': 'Dmytro', 'age': 18, 'friends': ['Ivanenko', 'Petrenko']}
print(p.__dict__)
# {'surname': <class 'str'>, 'name': <class 'str'>, 'age': <class 'int'>, 'friends': <class 'list'>}
print({k: v.__class__ for k, v in p.__dict__.items()})

print(hasattr(Person, 'count'))
print(hasattr(Person, 'COUNT'))
