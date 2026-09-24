a = [i ** 7 for i in range(12, 26)]
b = (i ** 7 for i in range(12, 26))
print(a)
while True:
    try:
        print(next(b), end=', ')
    except StopIteration:
        break
