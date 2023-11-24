from colorama import Fore
import sys


def main():
    print(Fore.RED + "error", file=sys.stderr)
    print("after error - 1")

    print(Fore.GREEN + "Green")
    print(Fore.RED + "error", file=sys.stderr)
    print("after error - 2")


if __name__ == "__main__":
    main()