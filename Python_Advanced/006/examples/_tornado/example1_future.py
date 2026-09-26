from tornado import gen
from tornado.ioloop import IOLoop

# створення фУтура
future = gen.Future()
future = gen.Task()


async def consumer():
    print('Waiting for boss')
    # чекаємо на результат від future, без блокування потоку
    product = await future
    print('Product was found: {}'.format(product))


async def producer():
    print('Produces is boss, please wait when boss will get up')
    # засипаємо на 5сек, після чого встановлюємо результат нашому футуру
    # після встановлення результату, consumer продовжить виконання
    await gen.sleep(5)
    future.set_result({
        'id': 10,
        'name': 'Mobile Phone'
    })


async def run_tasks():
    await gen.multi([
        producer(),
        consumer()
    ])


IOLoop.current().run_sync(run_tasks)
