import threading
import time
dead = True


def counter(thread):
    global dead
    count = 0
    while dead:
        count += 1
        print(f"{thread} and value = {count}")
        time.sleep(3)


def main():
    global dead
    obj_counter = threading.Thread(target=counter, name="counter", args=("counter thread ", ))
    obj_counter.start()
    print(f"1 - counter thread is alive or dead: {obj_counter.is_alive()}")
    print("press ENTER to stop the thread....")
    input()
    dead = False
    print(f"\n2 - counter thread is alive or dead: {obj_counter.is_alive()}")


if __name__ == "__main__":
    main()
