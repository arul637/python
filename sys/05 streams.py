import sys
import string


def main():
    print("Hello, there")
    name = input("Enter your name: ")
    digit = string.digits
    for i in digit:
        if i in name:
            sys.stderr.write("\nyou have digits in your name?\n")

            sys.exit(2)
    else:
        print(f"\nHello {name}, nice to meet you!")
        sys.exit(0)


if __name__ == "__main__":
    main()
