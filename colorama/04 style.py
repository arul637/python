from colorama import Fore, Style


def main():
    print(Style.NORMAL + Fore.RED + "Normal red colored text")
    print(Style.BRIGHT + Fore.RED + "Bright red colored text")
    print(Style.DIM + Fore.RED + "Dim red colored text")

    print(Style.NORMAL + Fore.YELLOW + "Normal yellow colored text")
    print(Style.BRIGHT + Fore.YELLOW + "Bright yellow colored text")
    print(Style.DIM + Fore.YELLOW + "Dim yellow colored text")

    print(Style.NORMAL + Fore.CYAN + "Normal cyan colored text")
    print(Style.BRIGHT + Fore.CYAN + "Bright cyan colored text")
    print(Style.DIM + Fore.CYAN + "Dim cyan colored text")

    print(Style.NORMAL + Fore.BLUE + "Normal blue colored text")
    print(Style.BRIGHT + Fore.BLUE + "Bright blue colored text")
    print(Style.DIM + Fore.BLUE + "Dim blue colored text")

    print("\nBefore reset")

    print(Style.RESET_ALL + Fore.RESET)

    print("After reset")


if __name__ == "__main__":
    main()
