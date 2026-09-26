'''
Завдання 2
Розробіть сокет-сервер на основі бібліотеки asyncio
'''
import asyncio


async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888
    )

    message = input("Enter message: ")

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(1024)

    print(data.decode())

    writer.close()
    await writer.wait_closed()


asyncio.run(main())