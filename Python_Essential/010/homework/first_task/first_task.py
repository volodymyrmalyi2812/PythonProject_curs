'''
Завдання 1

Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.

'''
import re


def get_word(text):
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'’]+", text.lower())

    all_words = {}

    for word in words:
        if word in all_words:
            all_words[word] += 1
        else:
            all_words[word] = 1
    return all_words


text = 'Hello world. this language is python'

result = get_word(text)

for word, count in result.items():
    print(word, count)
