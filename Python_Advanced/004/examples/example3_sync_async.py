import asyncio
import time
import inspect


def sync_worker(number, divider):
    print(f'Sync Worker started with values: {number} / {divider}')
    time.sleep(1)
    print(number / divider)


#используем async def
async def async_worker(number, divider):
    print(f'Async Worker started with values: {number} / {divider}')
    # Вместо yield from используем await
    await asyncio.sleep(3)
    print(number / divider)


# Оборачиваем весь асинхронный код в главную функцию
async def main():
    # 1. Синхронный вызов
    sync_worker(30, 10)

    # 2. Проверка на корутину
    # Для проверки самой функции правильно использовать inspect.iscoroutinefunction
    print("sync_worker - это корутина?", inspect.iscoroutinefunction(sync_worker))

    # Создаем объект корутины для проверки
    coro = async_worker(10, 2)
    # Для проверки созданного объекта используется inspect.iscoroutine
    print("coro - это корутина?", inspect.iscoroutine(coro))
    # Обязательно "дожидаемся" корутину, чтобы не было RuntimeWarning
    await coro

    # 3. Запуск задач (Task)
    task_list = [
        asyncio.create_task(async_worker(30, 10)),
        asyncio.create_task(async_worker(50, 25)),
    ]

    # Ждем завершения всех задач
    await asyncio.wait(task_list)


# Запускаем цикл событий (автоматически создает, выполняет и закрывает loop)
if __name__ == "__main__":
    asyncio.run(main())