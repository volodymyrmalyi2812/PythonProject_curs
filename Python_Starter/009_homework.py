"""
Завдання 1

Прочитайте у документації з мови Python інформацію про перелічені у резюме цього уроку стандартні функції. Перевірте їх на практиці.

Завдання 2

Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

Завдання 3

Нехай на кожну сходинку можна стати з попередньої або переступивши через одну. Визначте, скількома способами можна піднятися на задану сходинку.

Завдання 4

Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.

Завдання 5

Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї функції створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів) та функцію calc_rezult з формальними параметрами зовнішньої функції quadratic_equation. Всередині функції calc_rezult здійснити пошук дискримінанта, згідно з результатом якого зробити розрахунок коренів рівняння. Зовнішня функція quadratic_equation має повернути перелік значень коренів квадратного рівняння. Надати можливість користувачеві ввести з клавіатури формальні параметри для передачі їх у створену функцію quadratic_equation, результати роботи функції відобразити на екрані.
"""


"""
Завдання 2

Створіть програму, яка перевіряє, чи є паліндромом введена фраза
"""

# def check_sentence(sentence):
#     result_sentence = sentence.lower().replace(" ", "")
#
#     reversed_sentence = reversed(result_sentence)
#     result_reversed_sentence = "".join(reversed_sentence)
#
#     if result_sentence == result_reversed_sentence:
#         return f"Your sentence is a palindrome {result_reversed_sentence}"
#     else:
#         return f"Your sentence is not a palindrome  {result_reversed_sentence}"
#
# user_sentence = input("Enter your sentence: ")
# user_result_sentence = check_sentence(user_sentence)
# print(user_result_sentence)



"""
Завдання 3

Нехай на кожну сходинку можна стати з попередньої або переступивши через одну. Визначте, скількома способами можна піднятися на задану сходинку.
"""


def count_step(step_start, step_end):
    for step in range(step_start, step_end+1):
        if step_end > 0:
            step_start += 1
        else:
            return "enter valid end step"
    return

user_step_stop = int(input("Please enter your step that u wanna reach: "))
user_start_step = int(input("Please enter your start step: "))

result_step = count_step(user_step_stop, user_start_step)


print(result_step)