'''
Завдання 3

Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.
'''



import re

def last_three_symbols(text):
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’]+", text)

    for word in words:
        print(word[-3:])

user_text = input('please enter any sentence: ')

last_three_symbols(user_text)