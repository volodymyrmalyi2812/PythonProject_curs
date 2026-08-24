import asyncio


def highload_operation(value):
    result = 0
    for i in range(0, value):
        result += i
    return result


async def main():
    # asyncio.to_thread сам отправит функцию в пул потоков и вернет результат
    task1 = asyncio.create_task(asyncio.to_thread(highload_operation, 10_000_000))
    task2 = asyncio.create_task(asyncio.to_thread(highload_operation, 10_000_001))

    # Ждем выполнения обеих задач
    results = await asyncio.gather(task1, task2)
    print(f'Results are: {results}')


if __name__ == "__main__":
    asyncio.run(main())