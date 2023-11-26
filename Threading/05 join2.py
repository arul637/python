import threading
import time
done = True
count = 0


def thread1(thread):
    global done, count
    while done:
        count += 1
        print(f"{thread} value = {count}")
        time.sleep(0.5)


def thread2(thread):
    global done, count
    while done:
        print(f"{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def wait1(thread):
    global count
    for _ in range(10):
        print(f"{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def wait2(thread):
    global count
    print('\n')
    for _ in range(10):
        print(f"{thread} value = {count}")
        count += 1
        time.sleep(0.5)


def main():
    global done
    obj_thread1 = threading.Thread(target=thread1, args=("Thread 1 ", ), name="t1")
    obj_thread2 = threading.Thread(target=thread2, args=("Thread 2 ", ), name="t2")

    print("\nFirst wait 1 will finished after wait 2 and Multi threading will starts.....\n")

    """
        join() method is used to wait all the threats until the current thread finishes
    """
    # creating the wait 1 thread
    obj_wait1 = threading.Thread(target=wait1, args=("Wait 1 ", ), name="wait 1")
    # start the wait 1 thread
    obj_wait1.start()
    # creating the join() function for wait 1 thread, so all other threads will wait.
    obj_wait1.join()

    obj_wait2 = threading.Thread(target=wait2, args=("Wait 2 ", ), name="wait 2")
    obj_wait2.start()
    obj_wait2.join()

    obj_thread1.start()
    obj_thread2.start()

    input("\n\npress ENTER to stop\n\n")
    done = False


if __name__ == "__main__":
    main()
