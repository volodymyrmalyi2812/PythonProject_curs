my_file = open("some.txt", "w")
print("Ім'я файлу:", my_file.name)
print("Файл закритий:", my_file.closed)
print("У якому режимі файл відкритий:", my_file.mode)
# у скільки байтах від початку файлу ми зараз знаходимося:
print("Поточна позиція покажчика читання/запису у файлі (у байтах):", my_file.tell)
print("Поточна позиція покажчика читання/запису у файлі (у байтах):", my_file.tell())
my_file.close()
print("Файл закритий:", my_file.closed)
