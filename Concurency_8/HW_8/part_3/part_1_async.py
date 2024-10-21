import profile

import aiohttp
import asyncio
import time
import requests
from playsound import playsound

async def activ():
    resp = requests.get("http://google.com")
    print(resp.status_code)


async def main():
    for _ in range(10):
        await asyncio.create_task(activ())

if __name__ == '__main__':
    print("Start")
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
    playsound("archerready1.mp3")