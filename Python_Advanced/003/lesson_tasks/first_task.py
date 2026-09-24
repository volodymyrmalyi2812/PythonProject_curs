'''
OOP. 1
Назва
Кількостей
Ціна
Рік виготовлення
Виробник

Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.


*передати ваши створенни обэкти до ши, щоб вин зробив з них формат джейсон,
потим розпарсити ци обэкти до листа котрий у вас вже э
'''


import json


class Product:
    def __init__(self, name, amount, price, year, manufacturer):
        self.name = name
        self.amount = amount
        self.price = price
        self.year = year
        self.manufacturer = manufacturer

    def __str__(self):
        return (
            f"Назва: {self.name}\n"
            f"Кількість: {self.amount}\n"
            f"Ціна: {self.price} грн\n"
            f"Рік виготовлення: {self.year}\n"
            f"Виробник: {self.manufacturer}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "price": self.price,
            "year": self.year,
            "manufacturer": self.manufacturer
        }


# Создаём объекты
product_1 = Product("Ноутбук", 5, 35000, 2025, "Lenovo")
product_2 = Product("Телефон", 10, 28000, 2026, "Samsung")
product_3 = Product("Телевізор", 3, 42000, 2024, "LG")
product_4 = Product("Планшет", 7, 19000, 2025, "Apple")


# Добавляем объекты в список
products = [
    product_1,
    product_2,
    product_3,
    product_4
]


# Находим самый дорогой товар
most_expensive_product = max(products, key=lambda product: product.price)

print("Найдорожчий товар:")
print(most_expensive_product)


# Преобразуем объекты в список словарей
products_for_json = []

for product in products:
    products_for_json.append(product.to_dict())


# Записываем данные в JSON-файл
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products_for_json, file, ensure_ascii=False, indent=4)


# Читаем данные из JSON-файла
with open("products.json", "r", encoding="utf-8") as file:
    products_from_json = json.load(file)


# Создаём новый список объектов из данных JSON
new_products = []

for product_data in products_from_json:
    product = Product(
        product_data["name"],
        product_data["amount"],
        product_data["price"],
        product_data["year"],
        product_data["manufacturer"]
    )

    new_products.append(product)


print("\nТовари після читання JSON:")

for product in new_products:
    print(product)
    print("-" * 30)