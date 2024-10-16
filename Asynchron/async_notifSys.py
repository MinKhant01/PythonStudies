import asyncio

async def send_notification(notification_type, message, delay):
    await asyncio.sleep(delay)
    print(f"[{notification_type}] {message}")

async def main():
    math_class = asyncio.create_task(
        send_notification("Class Start", "Math Class is starting now!", 5)
    )
    english_class = asyncio.create_task(
        send_notification("Class Start", "English Class is starting now!", 3)
    )

    assignment1 = asyncio.create_task(
        send_notification("Assignment Due", "Assignment1 is due now!", 6)
    )
    assignment2 = asyncio.create_task(
        send_notification("Assignment Due", "Assignment 2 is due now!", 4)
    )

    study_group = asyncio.create_task(
        send_notification("Event Reminder", "Study Group Meeting is starting now!", 7)
    )

    await asyncio.gather(
        math_class, english_class, assignment1, assignment2, study_group
    )

    print("All notifications have been sent.")

asyncio.run(main())