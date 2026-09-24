class Foo:
    bar = True


Foo = type('Foo', (), {'bar': True})
print(Foo)

# Клас Foo, створений через метаклас type(), можна використовувати як звичайний клас:
# <class '__main__.Foo'>
print(Foo)

f = Foo()
# True
print(f.bar)


# можна успадковуватися від нього
class FooChild(Foo):
    pass


# <class '__main__.FooChild'>
print(FooChild())
# bar успадкований від Foo
# True
FooChild.bar


# Додамо методи до класу FooChild(). Для цього визначимо функцію та додамо її як атрибут.

def echo_bar(self):
    print(self.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
# False
hasattr(Foo, 'echo_bar')
# True
hasattr(FooChild, 'echo_bar')

my_foo = FooChild()
print(my_foo)
my_foo.echo_bar()
# True
print(my_foo)


# після динамічного створення класу додамо ще один метод


def echo_bar_more(self):
    print('yet another method')


FooChild.echo_bar_more = echo_bar_more
hasattr(FooChild, 'echo_bar_more')
# True
