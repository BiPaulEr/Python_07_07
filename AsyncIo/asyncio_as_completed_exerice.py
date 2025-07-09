import asyncio
import random

async def do_work(duration):
    await asyncio.sleep(duration)
    return f"Finished work in {duration} seconds"

async def main():
    durations = [3, 1, 4, 2]
    task_completed = 0
    tasks = [do_work(duration) for duration in durations]
    for task in asyncio.as_completed(tasks):
        result = await task
        task_completed = task_completed+1
        print(result, "tache completed", task_completed)

asyncio.run(main())