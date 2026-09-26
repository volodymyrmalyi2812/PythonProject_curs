'''
Завдання 1
Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень вихідного масиву. Додайте анотацію типів для вхідних і вислідних значень функції.
'''
def to_strings(numbers: list[int]) -> list[str]:
    result: list[str] = []

    for number in numbers:
        result.append(str(number))

    return result


numbers: list[int] = [1, 2, 3, 4, 5]

print(to_strings(numbers))


'''
Завдання 2
Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
Клас Directory має мати такі поля:
·        назва (name типу str);
·        батьківська тека (root типу Directory);
·        список файлів (список типу files, який складається з екземплярів File);
·        список підтек (список типу sub_directories, який складається з екземплярів Directory). 

Клас Directory має мати такі поля:
·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root для приймального екземпляра);
·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root. Метод також видаляє теку зі списку sub_directories);
·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас File нижче);
·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory. Метод видаляє файл зі списку files). 

Клас File має мати такі поля:
·        назва (name типу str);
·        тека (Directory типу Directory). 
'''
from __future__ import annotations
from typing import Optional


class Directory:
    def __init__(self, name: str, root: Optional[Directory] = None) -> None:
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: list[File] = []
        self.sub_directories: list[Directory] = []

    def add_sub_directory(self, directory: Directory) -> None:
        directory.root = self
        self.sub_directories.append(directory)

    def remove_sub_directory(self, directory: Directory) -> None:
        if directory in self.sub_directories:
            self.sub_directories.remove(directory)
            directory.root = None

    def add_file(self, file: File) -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        if file in self.files:
            self.files.remove(file)
            file.directory = None


class File:
    def __init__(self, name: str, directory: Optional[Directory] = None) -> None:
        self.name: str = name
        self.directory: Optional[Directory] = directory


main: Directory = Directory("Main")
photos: Directory = Directory("Photos")
documents: Directory = Directory("Documents")

file1: File = File("photo.jpg")
file2: File = File("homework.txt")

main.add_sub_directory(photos)
main.add_sub_directory(documents)

photos.add_file(file1)
documents.add_file(file2)

print(main.name)
print([directory.name for directory in main.sub_directories])
print([file.name for file in photos.files])
print([file.name for file in documents.files])

main.remove_sub_directory(photos)

print([directory.name for directory in main.sub_directories])

