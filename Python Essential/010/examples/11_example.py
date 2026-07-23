import re

result = re.findall(r'\w\w', 'Qwerty Admin')
print(result)
# Вилучення 2х послідовних символів
result = re.findall(r'\b\w.', 'Qwerty Admin')
print(result)
