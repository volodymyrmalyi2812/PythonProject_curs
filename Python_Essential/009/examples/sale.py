def get_ticket_price():
    price = 2000
    number = int(input('Номер замовлення: '))
    if number % 1000 == 0:
        price *= 0.8
    return price


def get_total_price():
    total = 0
    while input('Купити квиток? (off - завершити): ') != 'off':
        current_price = get_ticket_price()
        print('Ціна за квиток:', current_price)
        total += current_price
    print('Разом до оплати:', total)
