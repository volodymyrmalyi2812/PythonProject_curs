class Student:
    surname = 'Ivanov'
    name = 'Ivan'
    marks = 95


person = Student()

surname = getattr(person, 'surname')
# Ivanov
print(surname)

name = getattr(person, 'name')
# Ivan
print(name)

marks = getattr(person, 'marks')
# 95
print(marks)
