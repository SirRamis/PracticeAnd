import asyncio
import time
#import aiohttp
#import requests


def gen():
    x = 10
    print(x)
    yield x

async def example():
    print(100)


async def one():
    print("Start one")
    await asyncio.sleep(1)
    #time.sleep(1)
    print("Stop one")

async def two():
    print("Start two")
    await asyncio.sleep(2)
    #time.sleep(5)
    print("Stop two")

async def three():
    print("Start three")
    await asyncio.sleep(3)
    #time.sleep(4)
    print("Stop three")

async def main():
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())



if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)