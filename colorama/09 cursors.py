from colorama import Fore


def pos(x, y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'


def main():
    print(Fore.GREEN + pos(30, 30) + "This text in (30, 30)th position with green color")


if __name__ == "__main__":
    main()