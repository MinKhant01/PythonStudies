"""
import asyncio

async def task_with_lock(lock, task_id):
    print(f"Task {task_id} is waiting to acquire the lock.")
    async with lock:
        print(f"Task {task_id} has acquired the lock.")
        await asyncio.sleep(2)
    print(f"Task {task_id} has released the lock.")

async def background_task():
    for i in range(5):
        print(f"Background task is running ... {i}")
        await asyncio.sleep(0.5)
    
async def main():
    lock = asyncio.Lock()
    await asyncio.gather(
        task_with_lock(lock,1),
        task_with_lock(lock,2),
        background_task()
    )

asyncio.run(main())
"""

import threading
import time

def task_with_lock(lock, task_id):
    print(f"Task {task_id} is waiting to acquire the lock.")
    with lock:
        print(f"Task {task_id} has acquired the lock.")
        time.sleep(2)
    print(f"Task {task_id} has released the lock.")

def background_task():
    for i in range(5):
        print(f"Backgrond task is running ... {i}")
        time.sleep(0.5)

lock = threading.Lock()
thread1 = threading.Thread(target=task_with_lock, args=(lock,1))
thread2 = threading.Thread(target=task_with_lock, args=(lock,2))
background_thread = threading.Thread(target=background_task)

thread1.start()
background_thread.start()
thread2.start()

thread1.join()
thread2.join()
background_thread.join()