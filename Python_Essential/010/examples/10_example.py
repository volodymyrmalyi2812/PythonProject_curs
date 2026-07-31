import re

result = re.findall(r'.', 'Qwerty Admin')
print(result)

result = re.findall(r'\w', 'Qwerty Admin')
print(result)

result = re.findall(r'\w*', 'Qwerty Admin')
print(result)

result = re.findall(r'\w+', 'Qwerty Admin')
print(result)

# Вилучення першого слова
result = re.findall(r'^\w+', 'Qwerty Admin')
print(result)

# Вилучення останнього слова
result = re.findall(r'\w+$', 'Qwerty Admin')
print(result)

