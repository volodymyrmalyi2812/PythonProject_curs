"""
Практика
1   Поля
Прізвище
Амплуа
Вік
Кількість ігор
Кількість голів
Визначити найкращого форварда, і вивести відомості про футболістів, які зіграли менше 5-ти ігор.
------------------------------------------------------------
2   Поля
Прізвище
Група
Фізика
Інформ
Історія
Визначити середній бал оцінок з всіх предметів, і вивести відомості про ня про студентів, середній бал яких більший за 4 яких більше 4.
------------------------------------------------------------
3   Поля
Продавець
Найменування
Кількість
Ціна
Дата_продажу
Визначити кількість товарів, які продані менше року тому і вивести відомості про них.
"""





"""

1   Поля
Прізвище
Амплуа
Вік
Кількість ігор
Кількість голів
Визначити найкращого форварда, і вивести відомості про футболістів, які зіграли менше 5-ти ігор.
"""


# class Football:
#     def __init__(self, name, position, age, number_of_matches, number_of_goals):
#         self.name = name
#         self.position = position
#         self.age = age
#         self.number_of_matches = number_of_matches
#         self.number_of_goals = number_of_goals
#
#     def __str__(self):
#         return f"{self.name}, {self.position}, {self.age}, {self.number_of_matches}, {self.number_of_goals}"
#
# player_1 = Football("Player 1", position="for", age=20, number_of_matches=10, number_of_goals=8)
# player_2 = Football("Player 2", position="for", age=22, number_of_matches=15, number_of_goals=6)
# player_3 = Football("Player 3", position="for", age=24, number_of_matches=20, number_of_goals=25)
#
# football_players = [player_1, player_2, player_3]
#
# def best_player(football_player, position):
#     best_forward = None
#     max_goal = -1
#     for player in football_player:
#         if player.position == position and player.number_of_goals > max_goal:
#             max_goal = player.number_of_goals
#             best_forward = player
#     return f"best forward is {best_forward} with {max_goal} goals"
#
# get_best_player = best_player(football_players, "for")
# print(get_best_player)




"""
Прізвище
Група
Фізика
Інформ
Історія
Визначити середній бал оцінок з всіх предметів, і вивести відомості про ня про студентів, середній бал яких більший за 4 яких більше 4.
------------------------------------------------------------
"""



class School:
    def __init__(self, name, group, physics, informatics, history):
        self.name = name
        self.group = group
        self.physics = physics
        self.informatics = informatics
        self.history = history

    def __str__(self):
        return f"{self.group} {self.physics} {self.informatics} {self.history}"

student_1 = School("John", 1, 5, 5, 4)
student_2 = School("Bob", 2, 4, 3, 3)
student_3 = School("Ben", 3, 2, 2, 5)


students = [student_1, student_2, student_3]


def avg_grade(student_name, grade):
    best_student = None
    max_grade = -1
    for student in students:
        if student.name == student_name or student. == student_name: