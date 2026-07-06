def validate_email(address):
    if not "@" in address:
        raise ValueError("Email Addresses must contain @ sign")


try:
    validate_email("test.com")
except ValueError as ex:
    print("We can do some special invalid input handling here")
    print(ex) # это функция validate_email
finally:
    print("Finally always runs whether we succeed or not.")
