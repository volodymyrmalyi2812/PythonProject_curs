import re


class Football:
    def __init__(
            self,
            lastname,
            amplua,
            age,
            count_of_games,
            count_of_goals,
            phone,
            email
    ):
        self.__lastname = self.__validate_lastname(lastname)
        self.__amplua = self.__validate_amplua(amplua)
        self.__age = self.__validate_age(age)
        self.__count_of_games = self.__validate_games(count_of_games)
        self.__count_of_goals = self.__validate_goals(count_of_goals)
        self.__phone = self.__validate_phone(phone)
        self.__email = self.__validate_email(email)

    def __validate_lastname(self, value):
        if not isinstance(value, str) or not value.isalpha() or len(value) < 2:
            raise ValueError("Некоректне прізвище")

        return value

    def __validate_amplua(self, value):
        if not re.fullmatch(r"(for|wor|zah)", value):
            raise ValueError("Амплуа повинно бути: for, wor або zah")

        return value

    def __validate_age(self, value):
        if not isinstance(value, int) or value < 16:
            raise ValueError("Вік повинен бути не менше 16 років")

        return value

    def __validate_games(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість ігор не може бути від'ємною")

        return value

    def __validate_goals(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість голів не може бути від'ємною")

        return value

    def __validate_phone(self, value):
        if not isinstance(value, str):
            raise ValueError("Телефон повинен бути рядком")

        if not re.fullmatch(r"\+380\d{9}", value):
            raise ValueError(
                "Телефон повинен бути у форматі +380XXXXXXXXX"
            )

        return value

    def __validate_email(self, value):
        if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", value):
            raise ValueError("Некоректний email")
        return value

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

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @count_of_goals.setter
    def count_of_goals(self, value):
        self.__count_of_goals = self.__validate_goals(value)

    def goals_per_game(self):
        if self.__count_of_games == 0:
            return 0

        return round(
            self.__count_of_goals / self.__count_of_games,
            2
        )

    def __str__(self):
        return (
            f"Прізвище: {self.__lastname}, "
            f"амплуа: {self.__amplua}, "
            f"вік: {self.__age}, "
            f"ігри: {self.__count_of_games}, "
            f"голи: {self.__count_of_goals}, "
            f"телефон: {self.__phone}, "
            f"email: {self.__email}"
        )


f1 = Football(
    "Ivanov",
    "for",
    27,
    10,
    7,
    '+380991234567',
    "test@gmail.com"
)

print(f1)
print("Середня кількість голів за гру:", f1.goals_per_game())