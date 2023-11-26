"""
    Daemon Thread:-
        1. run in background
        2. stop automatically when all threads have been finished
        3. program will not wail for daemon thread to complete
"""

import threading
import time
count = 0
dead = True


def timer():
    global count, dead
    while dead:
        count += 1
        time.sleep(1)


def show_count():
    global count, dead
    while dead:
        print(f"value of count: {count}")
        time.sleep(0.5)


def main():
    global dead
    threading.Thread(target=timer).start()
    threading.Thread(target=show_count).start()

    input("\n\npress ENTER to exit? ")
    dead = False


if __name__ == "__main__":
    main()
