import re

string = 'test123@gmail.com, test123@mail.ru, test123@ukr.net'

result = re.findall(r'@\w+', string)
print(result)

result = re.findall(r'@\w+\.\w+', string)
print(result)

result = re.findall(r'@\w+\.(\w+)', string)
print(result)
