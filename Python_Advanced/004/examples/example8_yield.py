import asyncio

# 1. Заменяем декоратор на async def
async def test_cor(cor_index, number):
    result = 0
    for i in range(number):
        result += i
        # 2. Заменяем yield from на await
        await asyncio.sleep(1)
        # Используем современные f-строки для красоты
        print(f'Index: {cor_index} -> {i}')
    return result

async def main():
    # 3. Используем asyncio.gather для параллельного запуска задач
    # Это намного удобнее, чем создавать список и передавать его в wait()
    await asyncio.gather(
        test_cor(1, 3),
        test_cor(2, 4)
    )

# 4. Запускаем всё одной командой, избавляясь от get_event_loop()
if __name__ == '__main__':
    asyncio.run(main())