import json


class Laptop:
    def __init__(self, brand: str, screen_size: float, price: float, ram: int):
        self.__brand = brand
        self.__screen_size = screen_size
        self.__price = price
        self.__ram = ram

    def get_brand(self) -> str:
        return self.__brand

    def get_screen_size(self) -> float:
        return self.__screen_size

    def get_price(self) -> float:
        return self.__price

    def get_ram(self) -> int:
        return self.__ram

    def __str__(self) -> str:
        return f"Бренд: {self.__brand} | Екран: {self.__screen_size}\" | RAM: {self.__ram} ГБ | Ціна: ${self.__price}"


class AppleLaptop(Laptop):
    def __init__(self, screen_size: float, price: float, ram: int, model_name: str, chip_type: str):
        super().__init__("Apple", screen_size, price, ram)
        self.__model_name = model_name
        self.__chip_type = chip_type

    def get_model_name(self) -> str:
        return self.__model_name

    def get_chip_type(self) -> str:
        return self.__chip_type

    def __str__(self) -> str:
        return (
            f"Apple {self.__model_name} [{self.__chip_type}] | "
            f"Екран: {self.get_screen_size()}\" | RAM: {self.get_ram()} ГБ | Ціна: ${self.get_price()}"
        )


def find_largest_screen(laptops: list):
    return max(laptops, key=lambda laptop: laptop.get_screen_size()) if laptops else None


def find_smallest_screen(laptops: list):
    return min(laptops, key=lambda laptop: laptop.get_screen_size()) if laptops else None


def find_cheapest(laptops: list):
    return min(laptops, key=lambda laptop: laptop.get_price()) if laptops else None


def find_most_expensive(laptops: list):
    return max(laptops, key=lambda laptop: laptop.get_price()) if laptops else None


def find_max_ram(laptops: list):
    return max(laptops, key=lambda laptop: laptop.get_ram()) if laptops else None


def find_min_ram(laptops: list):
    return min(laptops, key=lambda laptop: laptop.get_ram()) if laptops else None


def laptop_to_dict(laptop) -> dict:
    if laptop is None:
        return None

    data = {
        "brand": laptop.get_brand(),
        "screen_size": laptop.get_screen_size(),
        "ram": laptop.get_ram(),
        "price": laptop.get_price()
    }

    if hasattr(laptop, 'get_model_name'):
        data["model_name"] = laptop.get_model_name()
    if hasattr(laptop, 'get_chip_type'):
        data["chip_type"] = laptop.get_chip_type()

    return data


def save_results_to_json(filename: str, results: dict):
    try:
        formatted_data = {category: laptop_to_dict(laptop) for category, laptop in results.items()}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(formatted_data, file, ensure_ascii=False, indent=4)
        print(f"Результати успішно збережено у файл '{filename}'")
    except IOError as e:
        print(f"Помилка під час запису у файл: {e}")


def dict_to_laptop(data: dict):
    if data is None:
        return None

    if "model_name" in data and "chip_type" in data:
        return AppleLaptop(
            screen_size=float(data["screen_size"]),
            price=float(data["price"]),
            ram=int(data["ram"]),
            model_name=data["model_name"],
            chip_type=data["chip_type"]
        )
    else:
        return Laptop(
            brand=data["brand"],
            screen_size=float(data["screen_size"]),
            price=float(data["price"]),
            ram=int(data["ram"])
        )


def load_results_from_json(filename: str) -> dict:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            raw_data = json.load(file)

        restored_results = {category: dict_to_laptop(laptop_data) for category, laptop_data in raw_data.items()}
        print(f"Дані успішно зчитано та відновлено з файлу '{filename}'\n")
        return restored_results
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return {}
    except json.JSONDecodeError:
        print(f"Помилка: у файлі '{filename}' некоректний JSON-формат.")
        return {}


class AnalyticsIterator:
    def __init__(self, data_dict: dict):
        self.__items = list(data_dict.items())
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.__index < len(self.__items):
            category, laptop = self.__items[self.__index]
            self.__index += 1

            if laptop:
                return f"📌 {category}:\n   ➔ {laptop}"
            else:
                return f"📌 {category}:\n   ➔ [Дані відсутні]"
        else:
            raise StopIteration


if __name__ == '__main__':
    laptops_database = [
        Laptop("Lenovo", 15.6, 800.0, 16),
        Laptop("Dell", 13.3, 650.0, 8),
        Laptop("Asus", 17.3, 1200.0, 32),
        AppleLaptop(14.2, 1999.0, 18, "MacBook Pro 14", "M3 Pro"),
        AppleLaptop(13.6, 1099.0, 8, "MacBook Air 13", "M2")
    ]

    analytics_results = {
        "Ноутбук з найбільшим екраном": find_largest_screen(laptops_database),
        "Ноутбук з найменшим екраном": find_smallest_screen(laptops_database),
        "Найдешевший ноутбук": find_cheapest(laptops_database),
        "Найдорожчий ноутбук": find_most_expensive(laptops_database),
        "Ноутбук з найбільшим RAM": find_max_ram(laptops_database),
        "Ноутбук з найменшим RAM": find_min_ram(laptops_database)
    }

    json_filename = "laptop_analytics.json"
    save_results_to_json(json_filename, analytics_results)

    restored_analytics = load_results_from_json(json_filename)

    print("=" * 60)
    print("       ФІНАЛЬНИЙ ЗВІТ АНАЛІТИКИ (ВИВІД ЧЕРЕЗ ІТЕРАТОР)")
    print("=" * 60)

    analytics_iterator = AnalyticsIterator(restored_analytics)

    for report_item in analytics_iterator:
        print(report_item)
        print("-" * 60)