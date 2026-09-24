'''
Завдання 4

Напишіть функцію, яка буде аналізувати текст, що надходить до неї,
і виводити тільки унікальні слова на екран,
загальну кількість слів і кількість унікальних слів.
'''


import re


def analyze_text(text):
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’]+",text.lower())

    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    print("Unique: ")

    for word in unique_words:
        print(word)

    print("Total number of words: ", len(words))
    print("Number of unique: ", len(unique_words))


user_text = input("please enter any text: ")

analyze_text(user_text)