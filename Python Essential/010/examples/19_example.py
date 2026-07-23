# Отримання кількості замін у рядку, в якому відбулась заміна
import re


string = "teSt1 test2 teSt3 test4 teSt5"
# re.subn(pattern, repl, string, count=0, flags=0)
# pattern - рядок шаблону регулярного виразу,
# repl - рядок заміни,
# string - рядок для пошуку,
# count=0 - максимальне число вхождень pattern,
# flags=0 - один або декілька прапарців.
result = re.subn(r"s", "x", string, flags=re.IGNORECASE)
print(result)
# Функція subn() модуля re виконує ту саму операцію, що й функція sub(), але повертає кортеж
# (new_string, number_of_subs_made), де
# new_string - рядок, отриманий у результаті заміни;
# number_of_subs_made - кількість виконаних замін.
