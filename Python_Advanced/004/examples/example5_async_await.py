import asyncio


async def async_worker(number, divider):
    """
    замість yield/yield from використовуємо синтаксис async/await.
    """
    print('Worker {} started'.format(number))
    await asyncio.sleep(2)
    print(number / divider)
    return number / divider


async def gather_worker():
    # виконання кількох завдань та отримання результату від кожної з них
    # в результаті виконання ми отримаємо список результатів у тому ж порядку,
    # у якому передавали співпрограми.
    result = await asyncio.gather(
        async_worker(50, 10),
        async_worker(60, 10),
        async_worker(70, 10),
        async_worker(80, 10),
        async_worker(90, 10),
    )
    print(result)


# Убираем старый event_loop и запускаем код по-современному:
if __name__ == "__main__":
    asyncio.run(gather_worker())