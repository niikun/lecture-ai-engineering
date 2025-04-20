import time
import asyncio
from datetime import datetime

async def wait_and_print(name):
    print(f"{name}を非同期処理開始")
    await asyncio.sleep(3)
    print(f"{name}を非同期処理終了")

async def run_async():
    start_time = datetime.now()
    task1 = asyncio.create_task(wait_and_print("A"))
    task2 = asyncio.create_task(wait_and_print("B"))
    await task1
    await task2
    end_time = datetime.now()
    delta = end_time - start_time
    print(f"実行時間: {delta.total_seconds()}秒")

if __name__ == "__main__":
    asyncio.run(run_async())