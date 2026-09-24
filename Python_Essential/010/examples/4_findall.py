import re

string = "Test1 Test2 Test3 Test4 Test5"

# re.findall(pattern, string) - призначений для пошуку за заданим шаблоном та повернення всіх знайдених значень
result = re.findall(r"Test", string)

print("Список усіх знайдених збігів:", result)
print("Кількість усіх збігів =", len(result))
