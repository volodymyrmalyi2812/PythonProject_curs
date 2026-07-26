'''
Завдання 3

Створіть список товарів в інтернет-магазині.
Серіалізуйте його за допомогою pickle та збережіть у JSON.
'''

import pickle
import json


products = [
    {
        "name": "Macbook",
        "price": 3000,
        "quantity": 2
    },
    {
        "name": "Mouse",
        "price": 30,
        "quantity": 10
    },
    {
        "name": "Keyboard",
        "price": 250,
        "quantity": 5
    }
]


with open("products.pkl", "wb") as file:
    pickle.dump(products, file)


with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii = False)

#ensure_ascii = False не только для англ но и для других языков
print("list was saved")