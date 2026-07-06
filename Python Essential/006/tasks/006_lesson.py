"""
OOP. 2
Виконавець
Жанр
Назва альбому
Тираж

Вивести дані про платівки, тираж яких перевищує 10000 примірників.



OOP. 1
Прізвище
Група
Фізика
Інформ
Історія

Визначити середній бал оцінок з фізики, кількість студентів з оцінкою 5 з інформатики та вивести відомості про них.
OOP. 2
Продавець
Найменування
Кількість
Ціна
Дата_продажу

Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити лити товар з максимальною вартістю.
OOP. 3
Найменування
Кількість
Ціна
Виробник
Дата_надходження_на_склад

Вивести відомості про товари з ціною вищою за середню.
 
"""




class Record:
    def __init__(self, name, genre, name_of_album, amount):
        self.__name = name
        self.__genre = genre
        self.__name_of_album = name_of_album
        self.__amount = amount

    @property
    def get_name(self):
        return self.__name

    @property
    def get_genre(self):
        return self.__genre

    @property
    def get_name_of_album(self):
        return self.__name_of_album

    @property
    def get_amount(self):
        return self.__amount

    def __str__(self):
        return f'{self.__name}, {self.__genre}, {self.__amount}, {self.__name_of_album}'






first_product = Record("Name1", "Genre1", "name_of_album", 10000)
second_product = Record("Name2", "Genre2", "name_of_album", 5000)
third_product = Record("Name3", "Genre3", "name_of_album", 23400)
fourth_product = Record("Name4", "Genre4", "name_of_album", 13000)
fifth_product = Record("Name5", "Genre5", "name_of_album", 4600)
sixth_product = Record("Name6", "Genre6", "name_of_album", 16000)


products = [first_product, second_product, third_product, fourth_product, fifth_product, sixth_product]



# def get_list_of_products():
#     for product in products:
#         get_amount = product.get_amount()
#         if get_amount > 10000:
#             print(product)
# get_list_of_products()

# или же тоже самое написать с итератором и while циклом, а не с циклом for и def



iterator = iter(products)
while True:
    try:
        product = next(iterator)

        if product.get_amount() > 10000:
            print(product)

    except StopIteration:
        break