import functools


def is_divider(number):
    print("Coroutine started")
    while True:
        # приймаємо значення у співпрограму через yield
        value = yield
        if number % value == 0:
            print(value)


# створення корутини
cor = is_divider(100)
# запуск корутини та виконання обчислень у тілі while
# програма зупиняється на yield
cor.send(None)
# передаємо число для обчислень однієї ітерації для присвоєння value
cor.send(11)
cor.send(18)
cor.send(20)
# закриває корутину
cor.close()


def coroutine(func):
    """
    Декоратор для автоматичного запуску корутини, щоб не виконувати
    cor.send(None).
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # запускаємо і повертаємо корутину
        res.send(None)
        return res

    return wrapper


@coroutine
def is_divider_cor(number):
    print("Coroutine started")
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider_cor(100)
# немає необхідності робити крок `cor.send(None)`, тому що він описаний у декораторі
cor.send(11)
cor.send(18)
cor.send(20)
cor.close()
