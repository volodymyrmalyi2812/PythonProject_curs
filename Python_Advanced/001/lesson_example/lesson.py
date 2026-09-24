from functools import reduce


class Footballer:
    # Конструктор класу з явною ініціалізацією приватних полів
    def init(self, lastname, amplua, age, count_of_games, count_of_goals):
        # Одразу створюємо захищені (приватні) поля
        self.lastname = lastname
        self.__amplua = amplua

        # Для полів з валідацією проводимо перевірку безпосередньо при створенні об'єкта
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Вік має бути більшим за 0")

        if count_of_games >= 0:
            self.__count_of_games = count_of_games
        else:
            raise ValueError("Кількість ігор не може бути від'ємною")

        if count_of_goals >= 0:
            self.__count_of_goals = count_of_goals
        else:
            raise ValueError("Кількість голів не може бути від'ємною")

    # --- Геттери та сетери для доступу до приватних полів ---

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def amplua(self):
        return self.__amplua

    @amplua.setter
    def amplua(self, value):
        self.__amplua = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Вік має бути більшим за 0")

    @property
    def count_of_games(self):
        return self.__count_of_games

    @count_of_games.setter
    def count_of_games(self, value):
        if value >= 0:
            self.__count_of_games = value
        else:
            raise ValueError("Кількість ігор не може бути від'ємною")

    @property
    def count_of_goals(self):
        return self.__count_of_goals

    @count_of_goals.setter
    def count_of_goals(self, value):
        if value >= 0:
            self.__count_of_goals = value
        else:
            raise ValueError("Кількість голів не може бути від'ємною")

    # Метод для зручного виведення інформації про об'єкт
    def __str(self):
        return f"{self.__lastname}, Амплуа: {self.__amplua}, Вік: {self.__age}, Ігор: {self.__count_of_games}, Голів: {self.__count_of_goals}"


# Створення списку об'єктів
footbolists = [
    Footballer('ln1', 'for', 27, 10, 7),
    Footballer('ln2', 'wor', 17, 11, 0),
    Footballer('ln3', 'for', 28, 5, 1),
    Footballer('ln4', 'zah', 37, 17, 3),
    Footballer('ln5', 'for', 47, 3, 2)
]
def best_forward(footbolist,aplua):
    best_f = None
    max_goal = -1
    for gravec in footbolist:
        if gravec.amplua == aplua and gravec.count_of_goals > max_goal:
            max_goal = gravec.count_of_goals
            best_f = gravec
    return best_f

# --- Визначення найкращого форварда ---
forwards = filter(lambda p: p.amplua == 'for', footbolists)
best_forward = reduce(lambda p1, p2: p1 if p1.count_of_goals > p2.count_of_goals else p2, forwards)

print("--- Найкращий форвард ---")
print(best_forward)

# --- Відомості про футболістів, які зіграли менше 5-ти ігор ---
print("\n--- Зіграли менше 5-ти ігор ---")
few_games_players = filter(lambda p: p.count_of_games < 5, footbolists)

for p in few_games_players:
    print(p)



# 1. Сортування за кількістю голів (за спаданням, від найкращих до найгірших)
# Параметр reverse=True розвертає список
# sorted_by_goals = sorted(footbolists, key=lambda p: p.count_of_goals, reverse=True)
#
# print("--- Топ бомбардирів ---")
# for p in sorted_by_goals:
#     print(f"{p.lastname} - Голів: {p.count_of_goals}")
#
#
# # 2. Сортування за віком (за зростанням, від наймолодших)
# sorted_by_age = sorted(footbolists, key=lambda p: p.age)
#
# print("\n--- Гравці за віком ---")
# for p in sorted_by_age:
#     print(f"{p.lastname} - Вік: {p.age}")
#
#
# # 3. Подвійне сортування (Спочатку за амплуа, а при збігу - за кількістю ігор)
# # Лямбда повертає кортеж, за яким Python сортує крок за кроком
# complex_sort = sorted(footbolists, key=lambda p: (p.amplua, p.count_of_games))
#
# print("\n--- Сортування: Амплуа + Ігри ---")
# for p in complex_sort:
#     print(f"{p.lastname} - Амплуа: {p.amplua}, Ігор: {p.count_of_games}")