class MyClass1:
    my_attr1 = 1
    my_attr2 = 2
    my_attr3 = 3


class MyClass2(MyClass1):
    pass


m_c = MyClass1()
print(isinstance(MyClass1(), MyClass1))
print(type(MyClass1() == MyClass1))
print(isinstance(MyClass2(), MyClass1))
print(type(MyClass2() == MyClass1))
print()
print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))
print(hasattr(m_c, "my_attr1"))
print(hasattr(m_c, "my_attr2"))
print(hasattr(m_c, "my_attr3"))
print(hasattr(m_c, "my_attr4"))
print()
print(isinstance(m_c.my_attr1, int))
print(isinstance(m_c.my_attr2, int))
print(isinstance(m_c.my_attr3, int))
print()
print(isinstance(m_c.my_attr1, str))
print(isinstance(m_c.my_attr2, str))
print(isinstance(m_c.my_attr3, str))
