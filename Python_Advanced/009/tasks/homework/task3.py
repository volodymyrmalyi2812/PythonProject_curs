'''
Завдання 3

Створити клас, у який дозволяє зберігати дані про студента:

- ім'я;

- прізвище;

- вік;

- середній бал.

Створіть список з 10 студентів-інстансів даного класу та протестуйте валідність даних використовуючи пакет unittest.
'''

import unittest


class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade


students = [
    Student("Anna", "Smith", 18, 10.5),
    Student("Max", "Brown", 19, 9.2),
    Student("John", "Wilson", 20, 8.7),
    Student("Kate", "Taylor", 18, 11.0),
    Student("Alex", "White", 21, 7.8),
    Student("Maria", "Green", 19, 10.1),
    Student("David", "Black", 20, 9.5),
    Student("Sofia", "Martin", 18, 11.4),
    Student("Daniel", "Clark", 22, 8.9),
    Student("Emma", "Walker", 19, 10.8)
]


class TestStudents(unittest.TestCase):

    def test_number_of_students(self):
        self.assertEqual(len(students), 10)

    def test_first_name(self):
        for student in students:
            self.assertIsInstance(student.first_name, str)
            self.assertTrue(student.first_name)

    def test_last_name(self):
        for student in students:
            self.assertIsInstance(student.last_name, str)
            self.assertTrue(student.last_name)

    def test_age_type(self):
        for student in students:
            self.assertIsInstance(student.age, int)

    def test_age(self):
        for student in students:
            self.assertGreater(student.age, 0)

    def test_grade_type(self):
        for student in students:
            self.assertIsInstance(student.average_grade, (int, float))

    def test_grade_min(self):
        for student in students:
            self.assertGreaterEqual(student.average_grade, 0)

    def test_grade_max(self):
        for student in students:
            self.assertLessEqual(student.average_grade, 12)


if __name__ == "__main__":
    unittest.main()