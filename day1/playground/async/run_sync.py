import time
from datetime import datetime

def wait_and_print(name):
    print(f"{name}を開始")
    time.sleep(3)
    print(f"{name}を終了")

def run_sync():
    start_time = datetime.now()
    wait_and_print("A")
    wait_and_print("B")
    end_time = datetime.now()
    delta = end_time - start_time
    print(f"実行時間: {delta.total_seconds()}秒")

if __name__ == "__main__":
    run_sync()