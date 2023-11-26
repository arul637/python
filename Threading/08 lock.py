import threading


def thread1():
    global value, lock
    lock.acquire()
    try:
        while value < 5000:
            value += 1
        print("thread 1 ", value)
    finally:
        lock.release()


def thread2():
    global value, lock
    lock.acquire()
    try:
        value = 4500
        while value < 6000:
            value += 1
        print("thread 2 ", value)
    finally:
        lock.release()


def main():
    global lock, value
    value = 10
    lock = threading.Lock()

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()