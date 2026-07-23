import sale

answer = input('Бажаєте відвідати Чемпіонат Світу з футболу? (так / ні): ').lower()
if answer == 'так':
    sale.get_total_price()
else:
    print('Шкода!')
