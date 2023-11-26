"""
    Daemon Thread:-
        1. run in background
        2. stop automatically when all threads have been finished
        3. program will not wail for daemon thread to complete
"""

import threading
import time
count = 0
dead1 = True
dead2 = True


def timer():
    global count, dead1
    while dead1:
        count += 1
        time.sleep(1)


def show_count():
    global count, dead2
    while dead2:
        print(f"value of count: {count}")
        time.sleep(0.5)


def main():
    global dead2, count
    daemon = threading.Thread(target=timer, daemon=True)
    daemon.start()
    threading.Thread(target=show_count).start()

    input("\n\npress ENTER to exit? \n\n")
    dead2 = False

    print("\nThe program is stopped, but in background daemon thread still runs...\n")
    # print(daemon.is_alive())
    print(f"\nwait for 3 seconds:- ")
    time.sleep(3)
    print(f"\nvalue of count: {count}")
    # print(daemon.is_alive())


if __name__ == "__main__":
    main()
    print("\nmain thread finished here..., then daemon thread also finished...")
