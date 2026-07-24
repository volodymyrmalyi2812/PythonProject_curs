'''
Завдання 1

Вивчити роботу інструментів, які розглядалися на занятті.

Завдання 2

Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message. Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

Завдання 3

Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

Завдання 4

Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

Завдання 5

Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах. Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.

Завдання 6

Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.
'''




'''
Завдання 2

Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message. 
Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message. 
Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__. 
Роздрукувати інформацію на екрані.

'''

# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.__surname = surname
#         self.__name = name
#         self.__age = age
#         self.__mob_phone = mob_phone
#         self.__email = email
#
#     @property
#     def surname(self):
#         return self.__surname
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def mob_phone(self):
#         return self.__mob_phone
#     @property
#     def email(self):
#         return self.__email
#
#
#     def get_contact(self):
#         return 'method get contact'
#
#     def sent_message(self):
#         return 'method get message'
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.__job = job
#
#     @property
#     def job(self):
#         return self.__job
#
#     def get_message(self):
#         return 'method get message'
#
#
#
#
# contact_1 = Contact('surname1', 'name1', 18, '+380111111', 'first@email')
# update_contact_1 = UpdateContact('surname2', 'name2', 18, '+380222222', 'second@email', 'engineer')
#
# print(contact_1.__dict__)
# print(update_contact_1.__dict__)
#
# print(UpdateContact.__base__)
# print(UpdateContact.__bases__)




'''
Завдання 3

Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). 
Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
'''



# class Contact:
#     def __init__(self, surname, name, age, mob_phone, email):
#         self.__surname = surname
#         self.__name = name
#         self.__age = age
#         self.__mob_phone = mob_phone
#         self.__email = email
#
#     @property
#     def surname(self):
#         return self.__surname
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def mob_phone(self):
#         return self.__mob_phone
#     @property
#     def email(self):
#         return self.__email
#
#
#     def get_contact(self):
#         return 'method get contact'
#
#     def sent_message(self):
#         return 'method sent message'
#
# class UpdateContact(Contact):
#     def __init__(self, surname, name, age, mob_phone, email, job):
#         super().__init__(surname, name, age, mob_phone, email)
#         self.__job = job
#
#     @property
#     def job(self):
#         return self.__job
#
#     def get_message(self):
#         return 'method get message'
#
#
#
#
# contact_1 = Contact('surname1', 'name1', 18, '+380111111', 'first@email')
# update_contact_1 = UpdateContact('surname2', 'name2', 18, '+380222222', 'second@email', 'engineer')
#
#
#
#
# print('hasattr')
#
# print(hasattr(contact_1, 'surname'))
# print(hasattr(contact_1, 'name'))
# print(hasattr(contact_1, 'age'))
# print(hasattr(contact_1, 'mob_phone'))
# print(hasattr(contact_1, 'email'))
# print(hasattr(contact_1, 'job'))
#
# print(hasattr(update_contact_1, 'surname'))
# print(hasattr(update_contact_1, 'name'))
# print(hasattr(update_contact_1, 'age'))
# print(hasattr(update_contact_1, 'mob_phone'))
# print(hasattr(update_contact_1, 'email'))
# print(hasattr(update_contact_1, 'job'))
#
#
# print('getattr')
# print(getattr(contact_1, 'surname'))
# print(getattr(contact_1, 'name'))
# print(getattr(contact_1, 'age'))
# print(getattr(contact_1, 'mob_phone'))
# print(getattr(contact_1, 'email'))
#
#
# print(getattr(update_contact_1, 'surname'))
# print(getattr(update_contact_1, 'name'))
# print(getattr(update_contact_1, 'age'))
# print(getattr(update_contact_1, 'mob_phone'))
# print(getattr(update_contact_1, 'email'))
# print(getattr(update_contact_1, 'job'))
#
#
# print("SETATTR")
#
# setattr(contact_1, "contact_surname", "new surname1")
# setattr(contact_1, "contact_name", "new name1")
# setattr(contact_1, "contact_age", 20)
# setattr(contact_1, "contact_mob_phone", "+380999999")
# setattr(contact_1, "contact_email", "new_first@email")
#
# setattr(update_contact_1, "contact_surname", "new surname2")
# setattr(update_contact_1, "contact_name", "new name2")
# setattr(update_contact_1, "contact_age", 25)
# setattr(update_contact_1, "contact_mob_phone", "+380888888")
# setattr(update_contact_1, "contact_email", "new_second@email")
# setattr(update_contact_1, "updateContact_job", "programmer")
#
# print(contact_1.__dict__)
# print(update_contact_1.__dict__)
#
#
# print("DELATTR")
#
# setattr(contact_1, "city", "Berlin")
# print(contact_1.__dict__)
#
# delattr(contact_1, "city")
# print(contact_1.__dict__)
#
# setattr(update_contact_1, "city", "Hamburg")
# print(update_contact_1.__dict__)
#
# delattr(update_contact_1, "city")
# print(update_contact_1.__dict__)




'''
Завдання 4

Використовуючи код з завдання 2, створити 2 екземпляри обох класів. 
Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.
'''

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.__surname = surname
        self.__name = name
        self.__age = age
        self.__mob_phone = mob_phone
        self.__email = email

    @property
    def surname(self):
        return self.__surname
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def mob_phone(self):
        return self.__mob_phone
    @property
    def email(self):
        return self.__email


    def get_contact(self):
        return 'method get contact'

    def sent_message(self):
        return 'method sent message'

class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.__job = job

    @property
    def job(self):
        return self.__job

    def get_message(self):
        return 'method get message'




contact_1 = Contact('surname1', 'name1', 18, '+380111111', 'first@email')
contact_2 = Contact('surname2', 'name2', 20, '+380222222', 'second@email')

update_contact_1 = UpdateContact('surname3', 'name3', 18, '+380333333', 'third@email', 'engineer')
update_contact_2 = UpdateContact('surname4', 'name4', 20, '+380444444', 'fourth@email', 'data scientist')


print('check contact 1')
print(isinstance(contact_1, Contact))
print(isinstance(contact_1, UpdateContact))

# показывает нам экземпляр класса то есть создан ли класс по шаблону другого

print('check contact 2')
print(isinstance(contact_2, Contact))
print(isinstance(contact_2, UpdateContact))

print('check update contact 1')
print(isinstance(update_contact_1, Contact))
print(isinstance(update_contact_1, UpdateContact))


print('check update contact 2')
print(isinstance(update_contact_2, Contact))
print(isinstance(update_contact_2, UpdateContact))


print('check issubclass')

print(issubclass(UpdateContact, Contact))
print(issubclass(Contact, UpdateContact))