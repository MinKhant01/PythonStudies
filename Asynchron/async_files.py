import asyncio

async def download_file(file_name, download_time):
    print(f"Starting download of {file_name}")
    await asyncio.sleep(download_time)
    print(f"Completed download of {file_name}")

async def main():
    download3 = asyncio.create_task(
        download_file("file3.txt",5)
    )
    download1 = asyncio.create_task(
        download_file("file1.txt",6)
    )
    download2 = asyncio.create_task(
        download_file("file2.txt",3)
    )
    
    await asyncio.gather(download2,download1,download3)

asyncio.run(main())

"""
await asyncio.gather(download1, download2, download3)
output:
// the execution before asyncio.sleep(delay) depends on the order of download#
Starting download of file1.txt
Starting download of file2.txt
Starting download of file3.txt
// the execution after asyncio.sleep(delay) depends on the delay assigned to each download#
Completed download of file2.txt
Completed download of file3.txt
Completed download of file1.txt
"""