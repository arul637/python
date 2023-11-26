import threading
import time


done = False


def thread1(thread):
    count = 0
    while not done:
        count += 1
        print(f"{thread} value = {count}")
        time.sleep(1)


def thread2(thread):
    count = 0
    while not done:
        count += 1
        print(f"{thread} value = {count}")
        time.sleep(1)


def thread_status():
    while not done:
        print(f"\n\nactive thread count: {threading.active_count()}")
        print(f"current thread: {threading.current_thread()}")
        print(f"enumeration number of threads: {threading.enumerate()}\n\n")
        time.sleep(10)


def main():
    obj_thread1 = threading.Thread(target=thread1, args=("Thread - 1", ))
    obj_thread2 = threading.Thread(target=thread2, args=("Thread - 2", ))

    obj_thread_status = threading.Thread(target=thread_status)

    obj_thread1.start()
    obj_thread2.start()

    obj_thread_status.start()


if __name__ == "__main__":
    main()
