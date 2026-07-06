class GetAttribute1:
    # атрибут класу GetAttribute1
    my_attr1 = 1

    def __init__(self):
        # атрибут екземпляру класу GetAttribute1
        self.my_attr2 = 2

    # Тільки для невизначенних атрибутів
    def __getattr__(self, my_attr):
        # Не attr1: наслідується від класу
        print('Get: ' + my_attr)
        # Не my_attr2: зберігається у екземплярі
        return 3


A = GetAttribute1()
print(A.my_attr1)
print(A.my_attr2)
# віртуальний атрибут, значення якого обчислюється при зверненні до нього
# перехоплює лише спроби звернення до атрибуту attr3, оскільки це єдиний невизначений аргумент.
print(A.my_attr3)
print('-' * 50)


class GetAttribute2(object):
    # атрибут класу GetAttribute2
    my_attr1 = 1

    def __init__(self):
        # атрибут екземпляру класу GetAttribute2
        self.my_attr2 = 2

    # Викликається всіма операціями присвоєння
    def __getattribute__(self, my_attr):
        # Для запобігання зацикленню використовується суперклас
        print('Get: ' + my_attr)
        if my_attr == 'my_attr3':
            return 3
        else:
            return object.__getattribute__(self, my_attr)


B = GetAttribute2()
print(B.my_attr1)
print(B.my_attr2)
# перехоплює всі спроби читання значень атрибутів і для отримання значень некерованих атрибутів має викликати метод
# суперкласу, щоб уникнути зациклювання
print(B.my_attr3)
# Незважаючи на те, що метод __getattribute__ перехоплює більше операцій звернення до атрибутів, ніж метод __getattr__,
# проте на практиці вони виявляються лише варіаціями на одну тему - якщо атрибути фізично не зберігаються в пам'яті,
# ці два методи дають один і той самий ефект.
