class MyClass:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @staticmethod
    def toChangeName(name):
        return name.replace("/", "-")


class UpdateClass(MyClass):
    def getName(self):
        return MyClass.toChangeName(self.name)


name1 = MyClass("25-07-2022")
ud_name1 = UpdateClass("25/07/2022")

if name1.getName() == ud_name1.getName():
    print("Equal")
else:
    print("Unequal")
