import asyncio

async def receive_message(user_name, message, delay):
    await asyncio.sleep(delay)
    print(f"{user_name}: {message}")

async def main():
    message1 = asyncio.create_task(
        receive_message("Alice", "Hello from Alice", 5)
    )
    message2 = asyncio.create_task(
        receive_message("Bob", "Hi from Bob", 4)
    )
    message3 = asyncio.create_task(
        receive_message("Charlie", "Konichiwa from Charlie",1)
    )
    await asyncio.gather(
        message1, message2, message3
    )

asyncio.run(main())