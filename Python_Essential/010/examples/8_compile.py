import re

string = "Test1 Test2 Test3 Test4 Test5"
# re.compile(pattern, repl, string) - можливість зібрати регулярне вираження в об'єкт, який у свою чергу можна
# # Використовувати для пошуку. Призначений для пошуку за заданим шаблоном і дозволяє уникнути переписування
# одного і того ж коду (вирази)
pattern = re.compile("T")
result1 = pattern.findall(string)
print(result1)
# Якщо шукане не знайшли, результат – порожній список
result2 = pattern.findall(string.lower())
print(result2)
