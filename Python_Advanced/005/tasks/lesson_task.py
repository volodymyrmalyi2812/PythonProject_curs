'''

Назва
Кількостей
Ціна
Рік виготовлення
Виробник

Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.

+ Найдешевший товар на склади

и вивести результат до консоли та у файл JSON

'''



import json


class Product:
    def __init__(self, name, quantity, price, year, manufacturer):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.year = year
        self.manufacturer = manufacturer

    def info(self):
        return {
            "Назва": self.name,
            "Кількість": self.quantity,
            "Ціна": self.price,
            "Рік виготовлення": self.year,
            "Виробник": self.manufacturer
        }


products = [
    Product("Ноутбук", 5, 35000, 2025, "Lenovo"),
    Product("Телефон", 10, 22000, 2026, "Samsung"),
    Product("Мишка", 20, 1200, 2024, "Logitech"),
    Product("Монітор", 7, 15000, 2025, "LG"),
    Product("Клавіатура", 15, 2500, 2024, "HyperX")
]


expensive = max(products, key=lambda x: x.price)
cheap = min(products, key=lambda x: x.price)


print("Найдорожчий товар:")
for key, value in expensive.info().items():
    print(key, ":", value)

print()

print("Найдешевший товар:")
for key, value in cheap.info().items():
    print(key, ":", value)


result = {
    "Найдорожчий товар": expensive.info(),
    "Найдешевший товар": cheap.info()
}


with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)