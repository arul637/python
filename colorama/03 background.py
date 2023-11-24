from colorama import Back, Fore


def main():
    print(Back.RED + Fore.YELLOW + "Background color to red and foreground color to yellow")
    print(Back.BLUE + Fore.WHITE + "Background color to blue and foreground color to white")
    print(Back.GREEN + Fore.YELLOW + "Background color to green and foreground color to yellow")
    print(Back.CYAN + Fore.RED + "Background color to cyan and foreground color to red")
    print(Back.BLACK + Fore.WHITE + "Background color to black and foreground color to white")

    print("\nAfter finished, the foreground and background color still remains same")

    print(Back.RESET + Fore.RESET)

    print("\nAfter reset, the foreground and background color been reset")


if __name__ == "__main__":
    main()