'''
Рік народження
Посада
Зарплата
Освіта

Визначити кількість працівників -
інженерів і надрукувати всі відомості про них.
+ Визначити найстаршого та наймолодшого працивника
+ зробити двома способами звичайною функциэю та лямбдою
'''

class Worker:
    def __init__(self, year, position, salary, education):
        self.year = year
        self.position = position
        self.salary = salary
        self.education = education

    def show(self):
        print("Рік народження:", self.year)
        print("Посада:", self.position)
        print("Зарплата:", self.salary)
        print("Освіта:", self.education)


workers = [
    Worker(1985, "інженер", 30000, "вища"),
    Worker(1998, "менеджер", 25000, "вища"),
    Worker(1975, "інженер", 35000, "вища"),
    Worker(2002, "програміст", 40000, "вища"),
    Worker(1995, "інженер", 28000, "середня")
]

engineers = []

for worker in workers:
    if worker.position == "інженер":
        engineers.append(worker)

print("Кількість інженерів:", len(engineers))

for worker in engineers:
    worker.show()
    print()


def get_year(worker):
    return worker.year


oldest = min(workers, key=get_year)
youngest = max(workers, key=get_year)

print("Найстарший працівник:")
oldest.show()

print()

print("Наймолодший працівник:")
youngest.show()

print()

oldest2 = min(workers, key=lambda x: x.year)
youngest2 = max(workers, key=lambda x: x.year)

print("Найстарший через lambda:")
oldest2.show()

print()

print("Наймолодший через lambda:")
youngest2.show()