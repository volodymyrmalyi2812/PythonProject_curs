
'''
If2. Дано ціле число. Якщо воно є додатним, то додати до нього 1; в іншому випадку відняти від нього 2. Вивести отримане число.
'''
from inspect import isfunction

# number = -4
# if number > 0:
#     number += 1
# else:
#     number -= 2
#
# print(number)

'''
If3. Дано ціле число. Якщо воно є додатним, то додати до нього 1; якщо від'ємним, то відняти від нього 2; якщо нульовим, то замінити його на 10. Вивести отримане число.
'''

# number = 5
# if number > 0:
#     number += 1
# elif number < 0:
#     number -= 2
# else:
#     number = 10
#
# print(number)

'''
If4 . Дано три цілих числа. Знайти кількість додатних чисел у вихідному наборі.
'''
# number_1 = 5
# number_2 = 6
# number_3 = 7
# count = 0
#
# if number_1 > 0:
#     count += 1
# if number_2 > 0:
#     count += 1
# if number_3 > 0:
#     count += 1
#
# print(count)



'''
If5. Дано три цілих числа. Знайти кількість додатних і кількість від'ємних чисел у вихідному наборі.
'''
# num_1 = 4
# num_2 = 5
# num_3 = 6
# positive_count = 0
# negative_count = 0
#
#
# if num_1 > 0:
#     positive_count += 1
# elif num_1 <0:
#     negative_count += 1
#
# if num_2 > 0:
#     positive_count += 1
# elif num_2 < 0:
#     negative_count += 1
#
# if num_3 > 0:
#     positive_count += 1
# elif num_3 < 0:
#     negative_count += 1
#
# print(f"There are {positive_count} positive numbers")
# print(f"There are {negative_count} negative numbers")



'''
If6 . Дано два числа. Вивести більше з них.
'''

# num_1 = 3
# num_2 = 3
# if num_1 > num_2:
#     print(f"The biggest number is {num_1}")
# elif num_1 < num_2:
#     print(f"the biggest number is {num_2}")
# else:
#     print("These numbers are same")

'''If7. Дано два числа. Вивести порядковий номер меншого з них.
'''
# num_1 = 8
# num_2 = 3
#
# if num_1 < num_2:
#     print(1)
# elif num_2 < num_1:
#     print(2)
# else:
#     print("These numbers are equal")



'''
If8. Дано два числа. Вивести спочатку більше, а потім менше з них.
'''
# num_1 = 5
# num_2 = 9
# if num_1 > num_2:
#     print(f"{num_1} is bigger that {num_2}")
# elif num_2 > num_1:
#     print(f"{num_2} is bigger that {num_1}")
# else:
#     print("Those numbers are equal")

'''
If9. Дано дві змінні дійсного типу: A, B. Перерозподілити значення даних змінних так, щоб в A виявилося менше зі значень, а в B - більше. 
Вивести нові значення змінних A і B.
'''
# A = 4
# B = 6
#
# if A < B:
#     A = A
#     print(f"The smallest number is {A}")
#     print(f"The largest number is {B}")
# elif B < A :
#     A = B
#     print(f"The smallest number is {A}")
# else:
#     print("Those numbers are equal")


'''
If10. Дано дві змінні цілого типу: A і B. Якщо їхні значення не рівні, то присвоїти кожній змінній суму цих значень, 
а якщо рівні, то присвоїти змінним нульові значення. Вивести нові значення змінних A і B.
'''
# A = 5
# B = 9
#
# if A != B:
#     sum_A = A + B
#     sum_B = B + A
#     print(f"A: {sum_A}, B: {sum_B}")
# else:
#     A = 0
#     B = 0
#     print(f"A: {A}, B: {B}")



'''
If11. Дано дві змінні цілого типу: A і B. Якщо їхні значення не рівні, то присвоїти кожній змінній більше з цих значень, 
а якщо дорівнюють, то присвоїти змінним нульові значення. Вивести нові значення змінних A і B.
'''

# A = 9
# B = 9
#
# if A != B:
#     if A > B:
#         B = A
#         print(f"A: {A}, B: {B}")
#     elif B > A:
#         A = B
#         print(f"B: {B}, A: {A}")
# else:
#     A = 0
#     B = 0
#     print(f"A: {A}, B: {B}")



'''
If12◦ . Дано три числа. Знайти найменше з них.
'''

# num_1 = 55
# num_2 = 55
# num_3 = 55
#
# if num_1 < num_2 and num_3:
#     print(f"The smallest number is {num_1}")
# elif num_2 < num_3 and num_1:
#     print(f"The smallest number is {num_2}")
# elif num_3 < num_1 and num_2:
#     print(f"The smallest number is {num_3}")
# else:
#     print("Those numbers are equal")

'''
If13. Дано три числа. Знайти середнє з них (тобто число, розташоване між найменшим і найбільшим).
'''
# num_1 = 3
# num_2 = 6
# num_3 = 5
#
# if num_1 < num_2 and num_1 < num_3:
#     min_value = num_1
# elif num_2 > num_1 and num_2 > num_3:
#     min_value = num_2
# else:
#     min_value = num_3
#
# if num_1 > num_2 and num_1 > num_3:
#     max_value = num_1
# elif num_2 > num_1 and num_2 > num_3:
#     max_value = num_2
# else:
#     max_value = num_3
#
# avg_value = (max_value + min_value) / 2
#
# print(f"Average value: {avg_value}")



'''
If14. Дано три числа. Вивести спочатку найменше, а потім найбільше з даних чисел.
'''
# num_1 = 3
# num_2 = 6
# num_3 = 5
#
# if num_1 < num_2 and num_1 < num_3:
#     min_value = num_1
# elif num_2 < num_1 and num_2 < num_3:
#     min_value = num_2
# else:
#     min_value = num_3
#
# if num_1 > num_2 and num_1 > num_3:
#     max_value = num_1
# elif num_2 > num_1 and num_2 > num_3:
#     max_value = num_2
# else:
#     max_value = num_3
#
# print(f"The smallest number is {min_value}")
# print(f"The biggest number is {max_value}")

'''
If15. Дано три числа. Знайти суму двох найбільших із них.
'''

# num_1 = 3
# num_2 = 6
# num_3 = 5
#
# if num_1 > num_2 and num_1 > num_3:
#     first_biggest_num = num_1
#     if num_2 >= num_3:
#         second_biggest_num = num_2
#     else:
#         second_biggest_num = num_3
#
# elif num_2 > num_1 and num_2 > num_3:
#     first_biggest_num = num_2
#     if num_1 >= num_2:
#         second_biggest_num = num_1
#     else:
#         second_biggest_num = num_3
# else:
#     first_biggest_num = num_3
#     if num_1 >= num_2:
#         second_biggest_num = num_1
#     else:
#         second_biggest_num = num_2
#
# sum_num = first_biggest_num + second_biggest_num
# print(f"The biggest sum number is {sum_num}")


'''
If16. Дано три змінні дійсного типу: A, B, C. 
Якщо їхні значення упорядковані за зростанням, то подвоїти їх; у протилежному випадку замінити значення кожної змінної на протилежне. 
Вивести нові значення змінних A, B, C.
'''
# num_1 = 3
# num_2 = 4
# num_3 = 5
#
# if num_1 < num_2 and num_2 < num_3:
#     num_1 = 2 * num_1
#     num_2 = 2 * num_2
#     num_3 = 2 * num_3
#     print(f"number 1 is {num_1}, number 2 is {num_2}, number 3 is {num_3}")
# else:
#     num_1 = -num_1
#     num_2 = -num_2
#     num_3 = -num_3
#     print(f"number 1 is {num_1}, number 2 is {num_2}, number 3 is {num_3}")


'''
# If17. Дано три змінні дійсного типу: A, B, C. 
# Якщо їхні значення упорядковані за зростанням або зменшенням, то подвоїти їх; у протилежному іншому випадку замінити значення кожної змінної на протилежне. 
# Вивести нові значення змінних A, B, C.
# '''
#
# A = 3
# B = 4
# C = 5
# if C > B and B > A:
#     A = A * 2
#     B = B * 2
#     C = C * 2
# elif A > B and B > C:
#     A = A * 2
#     B = B * 2
#     C = C * 2
# else:
#     A = -A
#     B = -B
#     C = -C
#
# print(f"A: {A}, B: {B}, C: {C}")
'''
If18. Дано три цілих числа, одне з яких відмінне від двох інших, рівних між собою. Визначити порядковий номер числа, відмінного від інших.
'''
# num_1 = 5
# num_2 = 5
# num_3 = 8
#
# if num_1 == num_2:
#     print(f"third number: {num_3} is not the same with first and second number")
# elif num_2 == num_3:
#     print(f"first number: {num_1} is not the same with third and second number")
# elif num_3 == num_1:
#     print(f"second number: {num_2} is not the same with first and third number")
# else:
#     print("All numbers are different")


'''
If19. Дано чотири цілих числа, одне з яких відмінне від трьох інших, рівних між собою. Визначити порядковий номер числа, відмінного від інших.
'''
# num_1 = 5
# num_2 = 5
# num_3 = 0
# num_4 = 5
#
#
# if num_1 == num_2 == num_3:
#     print(f"4th number: {num_4} is not the same")
# elif num_1 == num_4 == num_2:
#     print(f"third number: {num_3} is not the same")
# elif num_2 == num_3 == num_4:
#     print(f"first number: {num_1} is not the same")
# elif num_1 == num_3 == num_4:
#     print(f"second number: {num_2} is not the same with first and third number")
# else:
#     print("All numbers are different")

'''
If20. На числовій осі розташовані три точки: A, B, C. 
Визначити, яка з двох останніх точок (B або C) розташована ближче до A, і вивести цю точку та її відстань від точки A.
'''

# A = 6
# B = 70
# C = -1
# AB = abs(B - A)
# AC = abs(C - A)
#
# if AC < AB:
#     print (f"The smallest number to A is {AC}")
# elif AB < AC:
#     print(f"The smallest number to A is {AB}")
# else:
#     print("They are equal")

'''
If21. Дано цілочисельні координати точки на площині. Якщо точка збігається з початком координат, то вивести 0. 
Якщо точка не збігається з початком координат, але лежить на осі OX або OY, то вивести відповідно 1 або 2. 
Якщо точка не лежить на координатних осях, то вивести 3.
'''

# x = 5
# y = 8
#
# if x == 0 and y == 0:
#     print(0)
# elif y == 0:
#     print(1)
# elif x == 0:
#     print(2)
# else:
#     print(3)

'''
If22 . Дано координати точки, що не лежить на координатних осях OX і OY. Визначити номер координатної чверті, в якій знаходиться ця точка.
'''
# x = 5
# y = 8
#
# if y > 0 and x > 0:
#     print("The function is in the first quadrant")
# elif y > 0 and x < 0:
#     print("The function is in the second quadrant")
# elif y < 0 and x < 0:
#     print("The function is in the third quadrant")
# elif y < 0 and x > 0:
#     print("The function is in the fourth quadrant")
# else:
#     print("There is no function. Its only point")

