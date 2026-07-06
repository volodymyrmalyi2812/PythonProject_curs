class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


print(C.__base__)
print(C.__bases__)
