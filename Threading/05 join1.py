import threading
import time
done = True
count = 0


def thread1(thread):
    global done, count
    while done:
        count += 1
        print(f"\n{thread} value = {count}")
        time.sleep(0.5)


def thread2(thread):
    global done, count
    while done:
        print(f"\n{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def wait1(thread):
    global count
    for _ in range(100):
        print(f"\n{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def wait2(thread):
    global count
    for _ in range(100):
        print(f"\n{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def main():
    global done
    obj_thread1 = threading.Thread(target=thread1, args=("Thread 1 ", ), name="t1")
    obj_thread2 = threading.Thread(target=thread2, args=("Thread 2 ", ), name="t2")

    obj_wait1 = threading.Thread(target=wait1, args=("Wait 1 ", ), name="wait 1")
    obj_wait2 = threading.Thread(target=wait2, args=("Wait 2 ", ), name="wait 2")

    obj_thread1.start()
    obj_thread2.start()

    obj_wait1.start()
    obj_wait2.start()

    input("\n\npress ENTER to stop\n\n")
    done = False


if __name__ == "__main__":
    main()
