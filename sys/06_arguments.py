import sys


def main():
    count=0
    if len(sys.argv) < 3:
        sys.stderr.write(f"error: usage {sys.argv[0]} <filename> <word>")
        sys.stderr.flush()
        sys.exit(2)
    else:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                if sys.argv[2] in line:
                    count += 1
    print(f"The word `{sys.argv[2]}` present {count} times in `{sys.argv[1]}` file")


if __name__ == "__main__":
    main()