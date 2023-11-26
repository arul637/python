import threading
import time

done = False


def thread1(thread):
    global done
    count = 0
    while not done:
        count += 1
        print(f"{thread} and value = {count}")
        time.sleep(1)


def thread2(thread):
    global done
    count = 0
    while not done:
        count += 1
        print(f"{thread} and value = {count}")
        time.sleep(1)


def thread_status():
    while not done:
        print(f"\n\nactive thread count: {threading.active_count()}")
        print(f"current thread: {threading.current_thread()}")
        print(f"enumeration number of threads: {threading.enumerate()}\n\n")
        time.sleep(10)


def stop_thread():
    global done

    while not done:
        passcode = input("Enter the secret password to stop the program: ")
        time.sleep(3)
        if passcode == 'ak':
            done = True


def main():
    global done

    obj_thread1 = threading.Thread(target=thread1, args=("Thread - 1", ))
    obj_thread2 = threading.Thread(target=thread2, args=("Thread - 2", ))
    obj_thread_status = threading.Thread(target=thread_status)
    obj_stop_thread = threading.Thread(target=stop_thread)

#     starting the threads
    obj_thread1.start()
    obj_thread2.start()
    obj_thread_status.start()
    obj_stop_thread.start()


if __name__ == "__main__":
    main()
