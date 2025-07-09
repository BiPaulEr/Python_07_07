import asyncio
import random

async def read_file(file_name):
    wait_time = random.randint(0, 10)
    await asyncio.sleep(wait_time)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully with wait time {wait_time}")
    return(f"Contents of {file_name}")

def callback_done(task):
    print("Task is terminated ? ", task.done())
    #print("Task exception ? ", task.exception())
    print("Task result ? ", task.result())
    print("Task cancelled ? ", task.cancelled())


async def main():
    liste_task = []
    files = ["data/file1.txt", "data/file2.txt", "data/file3.txt"]
    for file in files:
        task = asyncio.create_task(read_file(file))
        liste_task.append(task)
        task.add_done_callback(callback_done)
    for task in liste_task:
        await task

asyncio.run(main())