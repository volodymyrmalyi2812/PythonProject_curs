def analyse(phrase):
    phrase = phrase.lower()
    res = phrase.find('розкл')
    if res != -1:
        print_schedule()

    res = phrase.find('тренер')
    if res != -1:
        print_trainer_info()

    res1 = phrase.find('оплат')
    res2 = phrase.find('грош')
    if res1 != -1 or res2 != -1:
        calc_money()


def print_schedule():
    print("Розклад тренувань:\nПН 15:00 - загальне силове тренування\nСР 15:00 - басейн\nПТ 17:00 - басейн")


def print_trainer_info():
    print('Головний тренер: Борисов Іван Сергійович, +380660231344')
    print('Тренер з плавання: Світлова Ірина Олегівна, +380502313234')


def calc_money():
    trainings = int(input('Скільки тренувань ви відвідали? '))
    print('До оплати:', trainings * 1500)
