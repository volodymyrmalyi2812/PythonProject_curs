import asyncio

async def async_worker(number, divider):
    print(f'Worker {number} started')
    await asyncio.sleep(0)
    print(number / divider)

async def main():
    # Создаем задачи
    task_list = [
        asyncio.create_task(async_worker(30, 10)),
        asyncio.create_task(async_worker(20, 10)),
    ]
    # Ждем выполнения всех задач
    await asyncio.wait(task_list)

# Запускаем цикл событий одной удобной командой
if __name__ == "__main__":
    asyncio.run(main())