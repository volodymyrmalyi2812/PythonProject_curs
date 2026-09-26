'''
Завдання 1
Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.
'''

# import json
#
# student = {
#     "name": "Alex",
#     "age": 18,
#     "city": "Hamburg"
# }
#
# car = {
#     "brand": "BMW",
#     "year": 2022,
#     "color": "black"
# }
#
# data = {
#     "student": student,
#     "car": car
# }
#
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
#
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#
# print(loaded_data)

'''

Завдання 2
Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH. Спробуйте здійснити пошук вмісту за створеним документом XML, ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.
'''
from lxml import etree

root = etree.Element("school")

student1 = etree.SubElement(root, "student")
student1.set("id", "1")

name1 = etree.SubElement(student1, "name")
name1.text = "Alex"

age1 = etree.SubElement(student1, "age")
age1.text = "18"

city1 = etree.SubElement(student1, "city")
city1.text = "Hamburg"

student2 = etree.SubElement(root, "student")
student2.set("id", "2")

name2 = etree.SubElement(student2, "name")
name2.text = "Max"

age2 = etree.SubElement(student2, "age")
age2.text = "20"

city2 = etree.SubElement(student2, "city")
city2.text = "Berlin"

tree = etree.ElementTree(root)
tree.write("school.xml", pretty_print=True, encoding="utf-8", xml_declaration=True)

tree = etree.parse("school.xml")

result1 = tree.xpath("//student/name/text()")
print(result1)

result2 = tree.xpath("//student[age > 18]/name/text()")
print(result2)

result3 = tree.xpath("//student[city='Hamburg']/name/text()")
print(result3)


'''
Завдання 3
Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. Зареєструйте створені діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.
'''
import csv

class MyDialect(csv.Dialect):
    delimiter = ";"
    quotechar = '"'
    escapechar = "\\"
    doublequote = True
    skipinitialspace = True
    lineterminator = "\n"
    quoting = csv.QUOTE_MINIMAL

csv.register_dialect("my_dialect", MyDialect)

data = [
    ["name", "age", "city"],
    ["Alex", 18, "Hamburg"],
    ["Max", 20, "Berlin"],
    ["Anna", 19, "Munich"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file, dialect="my_dialect")
    writer.writerows(data)

with open("people.csv", "r", newline="") as file:
    reader = csv.reader(file, dialect="my_dialect")

    for row in reader:
        print(row)


'''
Завдання 4
Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу. Поле «додаткові  характеристики матеріалу» має зберігати у собі масив, кожен елемент якого є кортежем із двох значень: перше – назва характеристики, а друге – її значення.
'''
import sqlite3
import pickle

connection = sqlite3.connect("materials.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    weight REAL,
    height REAL,
    characteristics BLOB
)
""")

characteristics1 = [
    ("color", "black"),
    ("type", "metal")
]

characteristics2 = [
    ("color", "white"),
    ("type", "plastic")
]

cursor.execute(
    "INSERT INTO materials VALUES (?, ?, ?, ?)",
    (1, 15.5, 120, pickle.dumps(characteristics1))
)

cursor.execute(
    "INSERT INTO materials VALUES (?, ?, ?, ?)",
    (2, 8.2, 80, pickle.dumps(characteristics2))
)

connection.commit()

cursor.execute("SELECT * FROM materials")

for row in cursor.fetchall():
    print(row[0], row[1], row[2], pickle.loads(row[3]))

connection.close()


'''
Завдання 5
Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, яка рахує середнє значення ваги всіх матеріалів вислідної вибірки й округляє значення до цілого.
'''
import sqlite3

class AverageWeight:
    def __init__(self):
        self.total = 0
        self.count = 0

    def step(self, weight):
        if weight is not None:
            self.total += weight
            self.count += 1

    def finalize(self):
        if self.count == 0:
            return 0

        return round(self.total / self.count)

connection = sqlite3.connect("materials.db")

connection.create_aggregate(
    "average_weight",
    1,
    AverageWeight
)

cursor = connection.cursor()

cursor.execute("""
SELECT average_weight(weight)
FROM materials
""")

print(cursor.fetchone()[0])

connection.close()



'''
Завдання 6
Для таблиці «матеріалу» з завдання 4 створіть функцію користувача, яка приймає необмежену кількість полів і повертає їх конкатенацію.
'''
import sqlite3

def concat(*values):
    result = []

    for value in values:
        if value is not None:
            result.append(str(value))

    return " ".join(result)

connection = sqlite3.connect("materials.db")

connection.create_function(
    "concat",
    -1,
    concat
)

cursor = connection.cursor()

cursor.execute("""
SELECT concat(id, weight, height)
FROM materials
""")

for row in cursor.fetchall():
    print(row[0])

connection.close()

'''
Завдання 7
Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль. Файл має містити такі стовпчики: імена, прізвища, дати народження та місто проживання. Реалізуйте можливості перезапису цього файлу, додавання нових рядків до наявного файлу, рядкового читання з файлу та конвертації всього вмісту у формати XML та JSON.
'''
import csv
import json
import xml.etree.ElementTree as ET

file_name = "people.csv"

def get_data():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    birthday = input("Enter birthday: ")
    city = input("Enter city: ")

    return [name, surname, birthday, city]


def write_file():
    data = get_data()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "surname", "birthday", "city"])
        writer.writerow(data)


def add_data():
    data = get_data()

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def read_file():
    with open(file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def to_json():
    with open(file_name, "r") as file:
        data = list(csv.DictReader(file))

    with open("people.json", "w") as file:
        json.dump(data, file, indent=4)


def to_xml():
    with open(file_name, "r") as file:
        data = list(csv.DictReader(file))

    root = ET.Element("people")

    for person in data:
        person_element = ET.SubElement(root, "person")

        for key, value in person.items():
            element = ET.SubElement(person_element, key)
            element.text = value

    tree = ET.ElementTree(root)
    tree.write("people.xml", encoding="utf-8", xml_declaration=True)


while True:
    print("1 - Write new file")
    print("2 - Add new person")
    print("3 - Read file")
    print("4 - Convert to JSON")
    print("5 - Convert to XML")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        write_file()

    elif choice == "2":
        add_data()

    elif choice == "3":
        read_file()

    elif choice == "4":
        to_json()

    elif choice == "5":
        to_xml()

    elif choice == "0":
        break