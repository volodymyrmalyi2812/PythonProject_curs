import asyncio
from asyncio.coroutines import iscoroutine
import time


def sync_worker(number, divider):
    print('Sync Worker started with values: {} / {}'.format(number, divider))
    time.sleep(1)
    print(number / divider)


@asyncio.coroutine
def async_worker(number, divider):
    """
    Навіщо писати свій декоратор, якщо Python 3.5 вже він є в asyncio.
    """
    print('Async Worker started with values: {} / {}'.format(number, divider))
    yield from asyncio.sleep(3)
    print(number / divider)


# sync
sync_worker(30, 10)
async_worker(30, 10)

# iscoroutine - дозволяє перевірити, чи є наша функція корутиною
# 1. випадок – ні.
print(iscoroutine(sync_worker))
# 2. випадок – так.
print(iscoroutine(async_worker(10, 2)))

# беремо цикл подій і обертаємо наші корутини в task-і для event loop
event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(50, 25)),
]
# створюємо загальне завдання, що містить у собі дві підзадачі.
# Це завдання чекатиме завершення перших двох.
tasks = asyncio.wait(task_list)
# запускаємо цикл подій до тих пір, поки не виконаються всі завдання.
event_loop.run_until_complete(tasks)
# закриваємо цикл подій та програма завершується.
event_loop.close()
