import asyncio

async def async_worker(seconds):
    print(f'Sleep using {seconds}')
    await asyncio.sleep(seconds)
    print(f'Done sleep: {seconds}')

async def resolve_future(future):
    await asyncio.sleep(5)
    print('Future set_result')
    future.set_result(10)

async def wait_for_future(future):
    result = await future
    print(f'Future result: {result}')

async def main():
    # Створюємо футур (asyncio.Future() - це сучасний і правильний спосіб)
    fut = asyncio.Future()

    # Створюємо завдання (tasks). Вони починають виконуватися одразу у фоні.
    asyncio.create_task(async_worker(3))
    asyncio.create_task(async_worker(4))
    asyncio.create_task(resolve_future(fut))
    asyncio.create_task(wait_for_future(fut))

    # Замість loop.stop() і run_forever() ми просто змушуємо
    # головну функцію почекати 13 секунд.
    # Коли main() завершить роботу, asyncio.run() сам усе зупинить і закриє.
    print('Stop in 13s')
    await asyncio.sleep(13)
    print('Stopped')

if __name__ == "__main__":
    asyncio.run(main())