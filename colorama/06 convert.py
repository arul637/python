from colorama import Back, Fore, Style, init


def main():
    init(convert=False, autoreset=True)  # won't work any color conversion, this work only in windows operating systems

    print(Style.BRIGHT + Fore.RED + Back.YELLOW + "red color text, with bright style and yellow background")
    print(Style.DIM + Fore.YELLOW + Back.BLACK + "yellow color text, with dim red style and black background")
    print(Style.NORMAL + Fore.GREEN + Back.RED + "green color text, with Normal style and red background")
    print(Style.BRIGHT + Fore.BLUE + Back.YELLOW + "blue color text, with Bright sytle and yellow background")
    print(Style.NORMAL + Fore.BLACK + Back.WHITE + "black color text, with Normal Style and white background")

    print("Without reset, by using autoreset in init(convert=False)")


if __name__ == "__main__":
    main()
