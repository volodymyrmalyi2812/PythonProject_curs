# Створення нескінченної послідовності
def all_even():
    n = 0
    while True:
        yield n
        n += 2


print(all_even())
a = all_even()
while True:
    print(next(a))
