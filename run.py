from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.GREEN + "zagon python aplikacije")

    print(Fore.CYAN + "odkrivam znanstveno fantastiko")

    for i in range(3):
        print(Fore.YELLOW + f"Korak {i+1}")

    print(Fore.RED + "konec :(")
    print(Style.DIM + "lalalalalal")


if __name__ == "__main__":
    main()