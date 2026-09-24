class Football:
    def __init__(self, lastname, amplua, age, count_of_games, count_of_goals):
        # Робимо атрибути захищеними (приватними) за допомогою __
        self.__lastname = lastname
        self.__amplua = amplua
        self.__age = age
        self.__count_of_games = count_of_games
        self.__count_of_goals = count_of_goals

    # --- Геттери (інтерфейс для безпечного читання даних) ---
    @property
    def lastname(self):
        return self.__lastname

    @property
    def amplua(self):
        return self.__amplua

    @property
    def age(self):
        return self.__age

    @property
    def count_of_games(self):
        return self.__count_of_games

    @property
    def count_of_goals(self):
        return self.__count_of_goals

    # --- Сеттери (приклад валідації даних при зміні) ---
    @count_of_goals.setter
    def count_of_goals(self, value):
        if value >= 0:
            self.__count_of_goals = value
        else:
            raise ValueError("Кількість голів не може бути від'ємною!")

    def __str__(self):
        return f"{self.__lastname}, {self.__amplua}, {self.__age}, {self.__count_of_games}, {self.__count_of_goals}"