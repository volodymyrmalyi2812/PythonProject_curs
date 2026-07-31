# example_4.py
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __test(self, b=None):
        self.a = 5
        self.b = b
        print(self.a, self.b)

    def setTest(self, c):
        self.__test(c)

    def getTest(self):
        return self.__test()


t = Test(1, 2)
# t._Test__test()
t.getTest()
t.setTest(10)
t.getTest()
