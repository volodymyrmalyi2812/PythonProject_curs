import re


def extract_data_from_file(input_file, output_file):
    try:
        # Читаем исходный файл
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Ищем даты формата 15.08.2000, 15-08-2000 или 15/08/2000
        dates = re.findall(
            r"\b\d{2}[./-]\d{2}[./-]\d{4}\b",
            text
        )

        # Ищем номера телефонов
        phones = re.findall(
            r"(?:\+380|0)\s?\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}",
            text
        )

        # Ищем электронные адреса
        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        # Записываем найденные данные в другой файл
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("Дати народження:\n")

            for date in dates:
                file.write(date + "\n")

            file.write("\nТелефони:\n")

            for phone in phones:
                file.write(phone + "\n")

            file.write("\nЕлектронні адреси:\n")

            for email in emails:
                file.write(email + "\n")

        print("Дані успішно записані у файл.")

    except FileNotFoundError:
        print("Початковий файл не знайдено.")

    except Exception as error:
        print("Виникла помилка:", error)


extract_data_from_file("input.txt", "result.txt")