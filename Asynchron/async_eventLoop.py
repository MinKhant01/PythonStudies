import asyncio
import time

async def periodic_task(interval, max_executions):
    for i in range(max_executions):
        print(f"Execution {i+1}: Current time is {time.strftime('%X')}")
        await asyncio.sleep(interval)
    print("Task completed.")

async def main():
    await periodic_task(3,5)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
