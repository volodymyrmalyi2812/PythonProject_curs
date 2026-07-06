def validate_email(address):
    assert "@" in address, "Email Addresses must contain @ sign"


try:
    validate_email("test.com")
except Exception as e:
    print(f'{e.__class__}: {e}')
finally:
    print("Finally always runs whether we succeed or not.")
