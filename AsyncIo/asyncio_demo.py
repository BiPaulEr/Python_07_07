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
    await asyncio.gather(worker("*"), worker("^"),worker("A"), worker("B"))


asyncio.run(main())