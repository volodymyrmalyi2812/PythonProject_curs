class A:
    """Some text"""
    x = 1

    def b(self):
        print(self.__dict__, "\n")
        print(dir(self))


a = A()
a.b()
print()
print(A.__dict__)
print()
print(a.__dict__)
