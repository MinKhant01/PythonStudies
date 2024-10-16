import asyncio

async def task1():
    await asyncio.sleep(2)
    print("task 1 completed")

async def task2():
    await asyncio.sleep(1)
    print("task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())