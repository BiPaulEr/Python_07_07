import asyncio
import aiofiles

async def read_file(file_name):
    async with aiofiles.open(file_name, "r", encoding="utf-8") as file:
        content = await file.read()
    return(f"Contents of {file_name} {content[:100]}")

async def main():
    liste_task = []
    for file in ["data/file1.txt", "data/file2.txt", "data/file3.txt"]:
        task = asyncio.create_task(read_file(file))
        liste_task.append(task)
    for task in liste_task:
        print(await task)

asyncio.run(main())