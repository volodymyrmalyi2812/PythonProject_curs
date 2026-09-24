import re


def extract_data_from_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            text = file.read()

        dates = re.findall(r"\b\d{2}[./-]\d{2}[./-]\d{4}\b",text)

        phones = re.findall(r"(?:\+380|0)\s?\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}",text)

        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text)

        with open(output_file, "w") as file:
            file.write("date of birth: ")

            for date in dates:
                file.write(date)

            file.write("/ phones: ")

            for phone in phones:
                file.write(phone)

            file.write("/ email: ")

            for email in emails:
                file.write(email)

        print("Dates found:", dates)
        print("Phones found:", phones)
        print("Emails found:", emails)

    except FileNotFoundError:
        print("file not found.")

    except Exception as error:
        print("error:", error)

extract_data_from_file("input.txt", "result.txt")