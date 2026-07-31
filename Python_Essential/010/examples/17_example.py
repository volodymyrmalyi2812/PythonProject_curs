import re

string = "1IvanovIvan2PetrovPetro3SydorovFedor4BondarenkoKristyna"
result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', string)
print(result)

result = re.findall(r'\d([A-Z][a-z]+)([A-Z][a-z]+)', string)
print(result)
