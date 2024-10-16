import asyncio

async def get_data(url):
    await asyncio.sleep(2)
    return {"data":f"{str(url)}"}

async def main():
    task1 = asyncio.create_task(get_data("https://www.sjsu.edu"))
    task2 = asyncio.create_task(get_data("https://www.apple.com"))
    result1, result2 = await asyncio.gather(task1, task2)
    print(result1)
    print(result2)

asyncio.run(main())