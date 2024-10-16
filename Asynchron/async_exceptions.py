import asyncio

async def faulty_coroutine():
    try:
        await asyncio.sleep(1)
        raise ValueError("An error occurred")
    except ValueError as e:
        print(f"Caught exception: {e}")