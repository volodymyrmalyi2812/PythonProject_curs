from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

event = Event()


async def consumer():
    print('Waiting for product')

    # очікуємо на події
    await event.wait()
    print('Product was found')

    # очищення події, для нового очікування
    event.clear()
    # очікування на повторне виникнення події
    await event.wait()
    print('Product was found twice')

    return 1


async def producer():
    print("About to set the event")

    # засинаємо на 5сек
    await gen.sleep(5)
    print('Set Event')

    # встановлення події
    event.set()
    # засипаємо на 5сек знову
    await gen.sleep(5)

    print('Set Event')
    # і знову встановлюємо подію
    event.set()

    return 2


async def runner():
    results = await gen.multi([
        producer(),
        consumer()
    ])
    print(results)


IOLoop.current().run_sync(runner)
