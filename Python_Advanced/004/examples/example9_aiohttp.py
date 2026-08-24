import asyncio
import time
import aiohttp
import requests

resources = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'http://example.com',
    'https://github.com',
    'https://jsonplaceholder.typicode.com/posts/1',
]


async def fetch_url(session, url):
    """
    Асинхронний HTTP клієнт для виконання запитів до сервера.
    """
    # 2. Используем session.get вместо aiohttp.request
    async with session.get(url) as response:
        return url, await response.text()


async def async_main():
    """
    Асинхронна корутина для виконання запитів.
    """
    started = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch_url(session, url))
            for url in resources
        ]


        for future in asyncio.as_completed(tasks):
            url, _ = await future
            print(url)

    # Используем f-строки
    print(f'Async spent time: {time.time() - started:.2f}s')


def sync_main():
    """
    Синхронна функція. Порівнюємо асинхронний та синхронний приклади.
    """
    started = time.time()
    for url in resources:
        requests.get(url)
        print(url)
    print(f'Sync spent time: {time.time() - started:.2f}s')


if __name__ == '__main__':
    print("--- Синхронний запуск ---")
    sync_main()

    print("\n--- Асинхронний запуск ---")

    asyncio.run(async_main())