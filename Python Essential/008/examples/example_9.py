def read_file():
    with open('quotes.txt', "r", encoding="UTF-8") as file:
        for line in file:
            print(line)


read_file()
author = input("Хто написав ці рядки? ")
with open('quotes.txt', "a", encoding="UTF-8") as file:
    file.write("(" + author + ")" + "\n")

while True:
    answer = input("Бажаєте додати ще одну цитату? (так / ні) ").lower()
    if answer == "так":
        quote = input("Введіть цитату: ")
        author = input("Введіть автора: ")
        file = open("quotes.txt", "a", encoding="UTF-8")
        file.write(quote + "\n" + "(" + author + ")" + "\n")
        file.close()
    else:
        break

read_file()
with open('quotes.txt', 'r', encoding="UTF-8") as file:
    for line in file:
        file.readline()

