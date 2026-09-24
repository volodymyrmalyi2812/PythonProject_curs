# import my_package

# my_package.my_module1 # AttributeError

# import my_package.my_module1
# import my_package.my_module2

# print(my_package.my_module1.b) # 20
# print(my_package.my_module2.d) # [1, 3, 5]

# 2-й варіант імпортування:
# from my_package import my_module1
# from my_package import my_module2

# print(my_module1.b) # 20
# print(my_module2.d) # [1, 3, 5]

# 3-й варіант імпортування:
from my_package.my_module1 import a
from my_package.my_module2 import h

# 10
print(a)
# Hello!
print(h)
