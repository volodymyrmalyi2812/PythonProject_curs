'''
Завдання 5

З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну адресу та відгук про курси учня.
Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.
'''

import re


def get_value(pattern, text, field_name):
    result = re.search(pattern, text, re.IGNORECASE)

    if result is None:
        return f"{field_name} not found"

    return result.group(1)


def extract_student_data(text):
    surname = get_value(r"Surname\s*:\s*([A-Za-z'-]+)", text, "surname")

    name = get_value(r"Name\s*:\s*([A-Za-z'-]+)",text,"name")

    date_of_birth = get_value(r"Date of birth\s*:\s*(\d{1,2}[./-]\d{1,2}[./-]\d{4})",text,"date of birth")

    email = get_value(r"Email\s*:\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})",text,"email")

    review = get_value(r"Review\s*:\s*(.+)",text,"review")

    student_data = {"surname": surname, "name": name, "date_of_birth": date_of_birth, "email": email, "review": review}

    return student_data


user_text = input("Enter student information: ")

result = extract_student_data(user_text)

print(result)