import asyncio


async def process_data(raw, timeout):
    try:
        await asyncio.sleep(timeout)

        # Пошли по трубам
        result = raw
        print(f'Logging value: {result}')  # pipe_1

        result += 10  # pipe_2
        print(f'Logging value: {result}')  # pipe_1

        result *= 2  # pipe_3
        print(f'Logging value: {result}')  # pipe_1

        result = 100 / result  # pipe_4
        print(f'Logging value: {result}')  # pipe_1

    except Exception as e:
        print(f'Error: {e}')  # error_1


async def main():
    await asyncio.gather(
        process_data(40, 2),
        process_data(-10, 2)
    )


if __name__ == '__main__':
    asyncio.run(main())