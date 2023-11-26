import threading
import time


def thread1(thread):
    for count in range(10):
        print(f"{thread} and value = {count}")
        time.sleep(0.5)


def thread2(thread):
    for count in range(10):
        print(f"{thread} and value = {count}")
        time.sleep(0.5)


def main():
    t1 = threading.Thread(target=thread1, args=("thread 1 ", ), name="Thread 1")
    t2 = threading.Thread(target=thread2, args=("thread 2 ", ), name="Thread 2")

    print(f"\nThread 1 ID before start: {t1.ident} ")
    t1.start()
    t1.join()
    print(f"Thread 1 ID after start: {t1.ident} ")

    print(f"Thread 2 ID before start: {t2.ident}")
    t2.start()
    print(f"Thread 2 ID after start: {t2.ident}")

    print(f"\nThread 1 ID after finished: {t1.ident}")
    print(f"Thread 2 ID after finished: {t2.ident}")


if __name__ == "__main__":
    main()
