import threading
import time
import concurrent.futures
import random

def printNum():
    for i in range(1,6):
        print(f"number: {i}")
        #delays function by seconds
        time.sleep(2)

def printLetters():
    for letters in "ABCDEF":
        print(f"Letters: {letters}")
        time.sleep(1)

def task(name):
    print(f"Task {name} starting")
    sleep_time = random.randint(1,5)
    time.sleep(sleep_time)
    print(f"Task {name} completed after {sleep_time}seconds")
    return sleep_time

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_to_task = {executor.submit(task, i): i for i in range(5)}
    for future in concurrent.futures.as_completed(future_to_task):
        task_name = future_to_task[future]
        try:
            result = future.result()
            print(f"Task {task_name} completed with result of {result}")
        except Exception as e:
            print(f"Task {task_name} generated an exception: {e}")

#Creates Threads
thread1 = threading.Thread(target=printNum)
thread2 = threading.Thread(target=printLetters)

#Start threads
#thread1.start()
#thread2.start()

#Ensures they work synchronously
#thread1.join()
#thread2.join()
