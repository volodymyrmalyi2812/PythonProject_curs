'''
Завдання 2
Розробіть сокет-сервер на основі бібліотеки asyncio
'''
import asyncio


async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")
    print("Client connected:", address)

    while True:
        data = await reader.read(1024)

        if not data:
            break

        message = data.decode()
        print("Received:", message)

        writer.write(("Server received: " + message).encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()

    print("Client disconnected")


async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888
    )

    print("Server started")

    async with server:
        await server.serve_forever()


asyncio.run(main())