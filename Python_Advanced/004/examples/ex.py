import asyncio
import time

# Уявіть, що ви — головний тренер, і вам потрібно перевірити детальну статистику кожного гравця,
# наприклад, зробивши запит до зовнішньої бази даних чи API. Якби ми робили це синхронно,
# ми б відправляли запит щодо першого гравця, чекали б на відповідь, потім переходили до другого,
# і так далі. Це дуже довго і в програмуванні називається блокуючим або послідовним виконанням.
#
# Але ми напишемо ефективний код і зробимо це асинхронно: ми ніби дамо завдання знайти інформацію
# одразу п'ятьом скаутам одночасно. Кожен витрачає час на пошук, але оскільки вони працюють паралельно,
# ми отримуємо всі результати за час виконання лише одного запиту. Для цього в нашому коді ми створимо
# спеціальну асинхронну функцію-імітатор, яка за допомогою await asyncio.sleep(1) імітуватиме цей довгий
# мережевий запит, при цьому не змушуючи всю програму зависати.
#
# Далі у головному циклі ми створимо окреме завдання для кожного футболіста за допомогою
# asyncio.create_task. А найцікавіше відбудеться далі: використовуючи функцію asyncio.gather,
# ми скажемо нашому коду запустити всі ці перевірки одночасно і дочекатися результатів. Головне,
# що ви маєте запам'ятати перед тим, як ми перейдемо до практики: асинхронність не прискорює роботу
# процесора чи математичні обчислення, її справжня суперсила — це боротьба з очікуванням.
# Якщо програмі треба чекати відповіді від бази даних або мережі, ми завжди використовуємо async/await.

class Football:
    def __init__(self, lastname, amplua, age, count_of_games, count_of_goals):
        self.__lastname = lastname
        self.__amplua = amplua
        self.__age = age
        self.__count_of_games = count_of_games
        self.__count_of_goals = count_of_goals

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

    @count_of_goals.setter
    def count_of_goals(self, value):
        if value >= 0:
            self.__count_of_goals = value
        else:
            raise ValueError("Кількість голів не може бути від'ємною!")

    def __str__(self):
        return f"Гравець: {self.__lastname}, Амплуа: {self.__amplua}, Голи: {self.__count_of_goals}"


# Асинхронна функція-імітатор: перевіряє гравця із затримкою (наприклад, запит до БД)
async def check_player(gravec, target_amplua):
    # Імітуємо затримку мережі або бази даних (1 секунда)
    await asyncio.sleep(1)

    # Повертаємо гравця, якщо амплуа збігається, інакше None
    if gravec.amplua == target_amplua:
        return gravec
    return None


# Головна асинхронна функція пошуку
async def best_forward_async(footbolist, amplua):
    print(f"Починаємо пошук найкращого гравця на позиції '{amplua}'...")
    start_time = time.time()

    # 1. Створюємо список асинхронних завдань для КОЖНОГО гравця
    tasks = [
        asyncio.create_task(check_player(gravec, amplua))
        for gravec in footbolist
    ]

    # 2. Запускаємо всі перевірки паралельно і чекаємо на їх завершення
    results = await asyncio.gather(*tasks)

    # 3. Відфільтровуємо порожні результати (тих, хто не підійшов за амплуа)
    matching_players = [player for player in results if player is not None]

    # 4. Знаходимо найкращого за кількістю голів
    if not matching_players:
        best_f = None
    else:
        # Використовуємо вбудовану функцію max для лаконічності
        best_f = max(matching_players, key=lambda p: p.count_of_goals)

    print(f"Пошук зайняв: {time.time() - start_time:.2f} сек")
    return best_f


# --- Тестові дані та запуск ---
async def main():
    f1 = Football('ln1', 'for', 27, 10, 7)
    f2 = Football('ln2', 'wor', 17, 11, 0)
    f3 = Football('ln3', 'for', 28, 5, 1)
    f4 = Football('ln4', 'zah', 37, 17, 3)
    f5 = Football('ln5', 'for', 47, 3, 2)

    footbolist_list = [f1, f2, f3, f4, f5]

    # Шукаємо найкращого форварда ('for')
    best = await best_forward_async(footbolist_list, 'for')
    print(f"\nРезультат: {best}")


# Стандартний запуск сучасного asyncio-коду
if __name__ == "__main__":
    asyncio.run(main())