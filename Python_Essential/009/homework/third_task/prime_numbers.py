def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(num_limit):
    prime_numbers = []

    for number in range(2, num_limit + 1):
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers

