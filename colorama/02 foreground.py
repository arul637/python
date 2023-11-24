from colorama import *


def main():
    print(Fore.RED + "this text in red color")
    print(Fore.BLUE + "this text in blue color")
    print(Fore.GREEN + "this text in green color")
    print(Fore.MAGENTA + "this text in magenta color")
    print(Fore.YELLOW + "this text in yellow color")
    print(Fore.LIGHTRED_EX + "this text in light red color")
    print(Fore.CYAN + "this text in cyan color")

    print("without color - 1")
    print("without color - 2")
    print("without color - 3")

    print("but, still cyan color")

    print(Fore.RESET)

    print("after, reset the color is set to default!")

if __name__ == "__main__":
    main()
