# example_5.py
class Test:
    def __init__(self, test_value):
        self.__private_attr = test_value

    def get_private_attr(self):
        return self.__private_attr

    @staticmethod
    def __private_function():
        print("I'm private")

    def call_private(self):
        self.__private_function()


test = Test(test_value=15)
print(test.get_private_attr())
test.call_private()
