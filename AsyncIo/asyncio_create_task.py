import asyncio
import time
async def worker_perso(caracter):
    time.sleep(1)
    for i in range(0, 10):
        print(caracter, flush=True, end="")
        time.sleep(1)

async def worker(caracter):
    await asyncio.sleep(1)
    for i in range(0, 10):
        print(caracter, flush=True, end="")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(worker("*"))
    task2 = asyncio.create_task(worker("i"))
    task3 = asyncio.create_task(worker("p"))

    await task1, task2, task3


asyncio.run(main())