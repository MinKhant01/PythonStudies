import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def wash():
    print("before wash")
    await asyncio.sleep(2)
    print("after wash")

async def main():
    #await asyncio.gather(count(), count(), count())
    await asyncio.gather(count(), wash(), count())

asyncio.run(main())