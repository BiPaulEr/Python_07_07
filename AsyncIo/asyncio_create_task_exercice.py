import asyncio

async def read_file(file_name):
    await asyncio.sleep(5)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

async def main():
    liste_task = []
    for file in ["data/file1.txt", "data/file2.txt", "data/file3.txt"]:
        task = asyncio.create_task(read_file(file))
        liste_task.append(task)
    for task in liste_task:
        await task

asyncio.run(main())