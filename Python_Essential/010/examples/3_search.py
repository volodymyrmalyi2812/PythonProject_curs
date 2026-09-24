import re

string = "Test1 Test2 Test3 Test4 Test3"

# re.search(pattern, string) - схожий на метод match(), але шукає не тільки на початку рядка,
# повертає лише перший знайдений збіг
result = re.search(r"Test3", string)
print(result.group())
print(result.group(0))

# IndexError: no such group
# print(result.group(1))
