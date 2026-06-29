"""
Завдання 1

Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр. Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

Завдання 2

Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

Завдання 3

Ознайомтеся зі спеціальними методами в Python, використовуючи посилання в кінці уроку, і навчіться використовувати ті з них, призначення яких ви можете зрозуміти. Повертайтеся до цієї теми протягом усього курсу та вивчайте спеціальні методи, що відповідають темам кожного уроку.

Завдання 4

Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу, і функцію продажу заданого автомобіля.

"""



"""
Завдання 1

Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр. 
Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.
"""



# class Book:
#     def __init__(self, author, title, year_of_publication, type):
#         self.author = author
#         self.title = title
#         self.year_of_publication = year_of_publication
#         self.type = type
#
#     def __str__(self):
#         return f'{self.author}, {self.title}, {self.year_of_publication}, {self.type}'
#
#     def __repr__(self):
#         return f' Book: {self.author}, {self.title}, {self.year_of_publication}, {self.type}'
#
#
# first_book = Book("Author1", "Title1", 2025, "Type1")
# second_book = Book("Author2", "Title2", 2024, "Type2")
# third_book = Book("Author3", "Title3", 2023, "Type3")
#
# books = [first_book, second_book, third_book]
#
# for book in books:
#     print(book) # для str
#
# print(books) # для repr



"""
Завдання 2

Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. 
Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.
"""
#
#
# class Book:
#     def __init__(self, author, title, year_of_publication, type, review):
#         self.author = author
#         self.title = title
#         self.year_of_publication = year_of_publication
#         self.type = type
#         self.review = review
#
#     def __str__(self):
#         return f'{self.author}, {self.title}, {self.year_of_publication}, {self.type}'
#
#     def __repr__(self):
#         return f' Book: {self.author}, {self.title}, {self.year_of_publication}, {self.type}'
#
#
# class BookReview:
#     def __init__(self, reviewer, review):
#         self.reviewer = reviewer
#         self.review = review
#
#     def __str__(self):
#         return f" Reviewer: {self.reviewer}, Review from 0 to 10 ->  {self.review}"
#
#
#
#
# first_review = BookReview("Reviewer1", 5)
# second_review = BookReview("Reviewer2", 10)
# third_review = BookReview("Reviewer3", 8)
#
#
# first_book = Book("Author1", "Title1", 2025, "Type1", [first_review])
# second_book = Book("Author2", "Title2", 2024, "Type2", [second_review])
# third_book = Book("Author3", "Title3", 2023, "Type3", [third_review])
#
#
# book_reviews = [first_book, second_book, third_book]
#
#
# for book in book_reviews:
#     print(book)
#     for review in book.review:
#         print(review)
#




"""
Завдання 4
Створіть клас, який описує автомобіль. 
Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу, 
і функцію продажу заданого автомобіля.
"""



class Car:
    def __init__(self, car, model, year):
        self.car = car
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.car}, {self.model}, {self.year}"

class CarDealership:
    def __init__(self, cars):
        self.cars = cars

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print("The car is not at the car dealership")
        else:
            print("Car is not available")


first_car = Car("Car1", "Model1", 2025)
second_car = Car("Car2", "Model2", 2024)
third_car = Car("Car3", "Model3", 2023)

cars_at_dealership = CarDealership([first_car, second_car, third_car])
cars_at_dealership.sell_car(first_car)

print(len(cars_at_dealership.cars))
for car in cars_at_dealership.cars:
    print(car)