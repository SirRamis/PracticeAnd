import aiohttp
import asyncio
import time

async def activ():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://google.com') as response:
            print(response.status)

async def run():
    start = time.time()
    tasks = [activ() for _ in range(100)]  # Создаем задачи
    await asyncio.gather(*tasks)  # Выполняем асинхронные задачи
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    asyncio.run(run())
