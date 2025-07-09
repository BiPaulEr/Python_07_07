import asyncio
import random
async def read_file(file_name):
    wait_time = random.randint(0, 10)
    await asyncio.sleep(wait_time)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully with wait time {wait_time}")
    return(f"Contents of {file_name}")

async def main():
    liste_task = []
    files = ["data/file1.txt", "data/file2.txt", "data/file3.txt"]
    print(await asyncio.gather(read_file(files[0]), read_file(files[1]),  read_file(files[2])))

asyncio.run(main())