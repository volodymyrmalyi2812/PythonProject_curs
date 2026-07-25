'''
OOP. 1
Прізвище
Вік
Кількість ігор
Кількість пропущених шайб

Визначити середній вік хокеїстів і вивести відомості про хокеїстів,
вік яких понад 25 років.

сделать метон принт де вывод буде через итераторы

'''

class Hockey:
    def __init__(self, surname, age, count_games, count_missing_goals):
        self.__surname = surname
        self.__age = age
        self.__count_games = count_games
        self.__count_missing_goals = count_missing_goals

    def __str__(self):
        return f'Surname: {self.__surname}, Age: {self.__age}, Count games: {self.__count_games}, Count missing goals: {self.__count_missing_goals}'

    @property
    def surname(self):
        return self.__surname
    @property
    def age(self):
        return self.__age
    @property
    def count_games(self):
        return self.__count_games
    @property
    def count_missing_goals(self):
        return self.__count_missing_goals

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('Age must be higher than 0')

    @count_games.setter
    def count_games(self, count_games):
        if count_games >= 0:
            self.__count_games = count_games
        else:
            raise ValueError('Count games must be higher than 0')

    @count_missing_goals.setter
    def count_missing_goals(self, count_missing_goals):
        if count_missing_goals > 0:
            self.__count_missing_goals = count_missing_goals
        else:
            raise ValueError('Count missing goals cannot be negative 0')


first_hockey_player = Hockey('surname1', 25, 13, 5)
second_hockey_player = Hockey('surname1', 21, 40, 10)
third_hockey_player = Hockey('surname1', 20, 35, 20)
fourth_hockey_player = Hockey('surname1', 38, 23, 1)
fifth_hockey_player = Hockey('surname1', 27, 50, 26)

players = [first_hockey_player, second_hockey_player, third_hockey_player, fourth_hockey_player, fifth_hockey_player]


def analyse_hockey_players(players):

    total_age = 0
    older_than_25 = []

    for player in players:
        total_age += player.age
        if player.age > 25:
            older_than_25.append(player)

    average_age = total_age / len(players)

    return older_than_25

def print_players(players):
    res = analyse_hockey_players(players)
    iter_players = iter(res)
    while True:
        try:
            player = next(iter_players)
            print(player)
        except StopIteration:
            continue



print_players(players)