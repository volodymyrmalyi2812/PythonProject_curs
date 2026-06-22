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


# def count_step(step):
#     if step < 0:
#         return "Enter valid step"
#     elif step == 0 or step == 1:
#         return 1
#
#     first_step = 1
#     second_step = 1
#
#     for current_step in range(2, step + 1):
#         result_step = first_step + second_step
#         first_step = second_step
#         second_step = result_step
#
#     return second_step
#
# user_step = int(input("Please enter your step that u wanna reach: "))
#
#
# result_step = count_step(user_step)
#
#
# print(result_step)






"""

Завдання 4

Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.
"""


#
# def count_numbers(first_number, second_number):
#     if first_number == second_number:
#         return first_number
#
#     return first_number + count_numbers(first_number + 1, second_number)
#
# result = count_numbers(1, 5)
# print(result)



"""
Завдання 5

Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. 
Усередині цієї функції створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів) 
та функцію calc_rezult з формальними параметрами зовнішньої функції quadratic_equation. 
Всередині функції calc_rezult здійснити пошук дискримінанта, згідно з результатом якого зробити розрахунок коренів рівняння. 
Зовнішня функція quadratic_equation має повернути перелік значень коренів квадратного рівняння. 
Надати можливість користувачеві ввести з клавіатури формальні параметри для передачі їх у створену функцію quadratic_equation, результати роботи функції відобразити на екрані.
"""




def quadratic_equation(a, b, c):
    x1 = None
    x2 = None


    def calc_result(a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b + discriminant ** 0.5 ) / (2 * a)
            x2 = (-b - discriminant ** 0.5 ) / (2 * a)

            return x1, x2
        else:
            return "please enter valid a, b, c numbers"
    x1 , x2 = calc_result(a, b, c)
    return x1 , x2



result = quadratic_equation(1, 5, 3)
print(result)