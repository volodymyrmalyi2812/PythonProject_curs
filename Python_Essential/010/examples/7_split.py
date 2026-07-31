import re

string = "test1 test2 test3 test4 test5"

# re.split(pattern, string, [maxsplit=0]) - призначений для поділу рядка за заданим шаблоном
# Стільки поділів, скільки це можливо
result = re.split(r"t", string)
print(result)

# maxsplit - кількість поділів
result = re.split(r"t", string, maxsplit=5)
print(result)

# maxsplit - кількість поділів
result = re.split(r"t", string, maxsplit=10)
print(result)
