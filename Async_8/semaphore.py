import aiohttp
import asyncio
import time

# Ограничение на количество одновременных запросов
semaphore = asyncio.Semaphore(10)


async def activ():
    async with semaphore:  # Используем семафор для ограничения
        async with aiohttp.ClientSession() as session:
            async with session.get('http://google.com') as response:
                status = response.status
                text = await response.text()
                print(status)
                return status, text  # Возвращаем и статус, и текст


async def run():
    start = time.time()

    tasks = [activ() for _ in range(100)]  # Создаем 100 задач для выполнения
    await asyncio.gather(*tasks)  # Выполняем все задачи асинхронно

    end = time.time()
    print(f"Время выполнения: {end - start:.2f} секунд")


if __name__ == '__main__':
    asyncio.run(run())
