'''
Завдання 1
Створіть функцію для обчислення факторіала числа.
Запустіть декілька завдань, використовуючи Thread, і заміряйте швидкість їхнього виконання,
а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на ThreadPoolExecutor.
Як приклади використовуйте останні значення, від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.
'''
import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def factorial(number):
    return math.factorial(number)


numbers = [10000, 20000, 30000, 40000]


start = time.time()

threads = []

for number in numbers:
    thread = threading.Thread(target=factorial, args=(number,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print("Thread time:", end - start)


start = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(factorial, numbers)

end = time.time()

print("ThreadPoolExecutor time:", end - start)


'''
Завдання 2
Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!». 
Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!». 
За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу. 
Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.
'''
import os
import time
import threading

event = threading.Event()
file_name = "test.txt"


def find_file():
    while True:
        if os.path.exists(file_name):
            return

        print("File not found")
        time.sleep(5)


def find_wow():
    while True:
        find_file()

        with open(file_name, "r") as file:
            text = file.read()

        if "Wow!" in text:
            print("Wow! found")
            event.set()
            return

        print("Wow! not found")
        time.sleep(5)


def delete_file():
    event.wait()

    if os.path.exists(file_name):
        os.remove(file_name)
        print("File deleted")


thread1 = threading.Thread(target=find_wow)
thread2 = threading.Thread(target=delete_file)

thread1.start()
thread2.start()

thread1.join()
thread2.join()