import re

string = "test1 test2 test3 test4 test5"

# re.sub(pattern, repl, string) - призначений для пошуку за заданим шаблоном і замінює вказаний підрядок
result = re.sub(r"t", "T", string)
print(result)

# Якщо шукане не знайшли, рядок залишається незмінним
result = re.sub(r"I", "A", string)
print(result)
