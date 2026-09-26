import asyncio


async def async_worker(seconds):
    print('Sleep using {}'.format(seconds))
    await asyncio.sleep(seconds)
    print('Done sleep: {}'.format(seconds))


async def stop_event_loop(loop, seconds):
    print('Stop in {}s'.format(seconds))
    await asyncio.sleep(seconds)
    loop.stop()
    print('Stopped')


async def resolve_future(future):
    await asyncio.sleep(5)
    print('Future set_result')
    future.set_result(10)


async def wait_for_future(future):
    result = await future
    print('Future result: {}'.format(result))


event_loop = asyncio.get_event_loop()

# створюємо футур і передамо його в корутину.
# в іншій корутині будемо чекати результату від цього футура.
# fut = event_loop.create_future()
fut = asyncio.Future()

# додаємо до циклу подій два завдання
event_loop.create_task(async_worker(3))
event_loop.create_task(async_worker(4))

# зупиняємо цикл подій, незалежно від успішності завершення у ньому завдань.
event_loop.create_task(stop_event_loop(event_loop, 13))

# у цій задачі ми встановимо результат футура
event_loop.create_task(resolve_future(fut))

# в цьому завданні ми чекатимемо результату футура
event_loop.create_task(wait_for_future(fut))

# запускаємо нескінченний цикл подій, але оскільки вище ми додали завдання
# для його зупинки, через 13 секунд ми вийдемо з нього.
event_loop.run_forever()
event_loop.close()
