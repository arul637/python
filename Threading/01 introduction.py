import threading


def main():
    print(f"current thread: {threading.current_thread()}")
    print(f"active thread count: {threading.active_count()}")
    print(f"enumeration number of threads: {threading.enumerate()}")


if __name__ == "__main__":
    main()