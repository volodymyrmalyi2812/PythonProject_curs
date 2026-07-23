from sport_salary import *

surname = input('Прізвище тренера: ')
job = input('Зайнятість (1-повна, 2-погодинна): ')
if job == '1':
    experience = int(input('Стаж у роках: '))
    salary = get_full_time(experience)
elif job == '2':
    hours = int(input('Відпрацьовано годин: '))
    salary = get_part_time(hours)
print(surname, '-', salary)
