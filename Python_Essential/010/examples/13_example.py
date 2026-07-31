import re

string = 'name: Admin, birthday: 01-12-2000, certificate: 01-06-2022'

result = re.findall(r'\d{2}-\d{2}-\d{4}', string)
print(result)

result = re.findall(r'\d{2}-\d{2}-(\d{4})', string)
print(result)
