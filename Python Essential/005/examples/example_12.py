class MyClass:
    my_attr = 1


m_c = MyClass()
m_c.my_attr = 54
print(hasattr(m_c, 'my_attr'))
print(m_c.my_attr)
delattr(m_c, 'my_attr')
print(hasattr(m_c, 'my_attr'))
print(m_c.my_attr)
