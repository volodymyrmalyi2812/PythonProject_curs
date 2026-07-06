class Footbal:
    def __init__(self, lastname, amplua, age, count_of_games, count_of_goals):
        self.lastname = lastname
        self.__amplua = amplua
        self.__age = age
        self.__count_of_games = count_of_games
        self.__count_of_goals = count_of_goals

    # --- Гетери (отримання даних) ---
    def get_lastname(self):
        return self.__lastname

    def get_amplua(self):
        return self.__amplua

    def get_age(self):
        return self.__age

    def get_games(self):
        return self.__count_of_games

    def get_goals(self):
        return self.__count_of_goals

    # --- Сетер (з перевіркою) ---
    def set_goals(self, goals):
        if goals >= 0:
            self.__count_of_goals = goals
        else:
            raise ValueError("Кількість голів не може бути від'ємною")

    def __str(self):
        return f"{self.__lastname}, {self.__amplua}, {self.__age}, {self.__count_of_games}, {self.__count_of_goals}"


# --- Створення об'єктів ---
f1 = Footbal("ln1",'for',27, 10, 7)
f2 = Footbal('ln2','wor',17, 11, 0)
f3 = Footbal('ln3','for',28, 5, 1)
f4 = Footbal('ln4','zah',37, 17, 3)
f5 = Footbal('ln5','for',47, 3, 2)

footbolist = [f1, f2, f3, f4, f5]


# --- Функція пошуку найкращого гравця ---
def best_forward(footbolist, amplua):
    best_f = None
    max_goal = -1
    try:
        for gravec in footbolist:
            if gravec.get_amplua() == amplua and gravec.get_goals() > max_goal:
                max_goal = gravec.get_goals()
                best_f = gravec

        if best_f is None:
            raise ValueError("Гравця з такою позицією не знайдено")

        return best_f

    except Exception as e:
        print(f"Помилка: {e}")
        return None


try:
    result = best_forward(footbolist, 'wor')
    if result:
        print(result)
except Exception as e:
    print(f"Помилка при виклику: {e}")