from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.GREEN + "Aplikacija se je uspešno zagnala!")

    print(Fore.CYAN + "Izvajam neko logiko...")

    for i in range(3):
        print(Fore.YELLOW + f"Korak {i+1}")

    print(Fore.RED + "Konec programa.")
    print(Style.DIM + "To je demo aplikacija za Docker nalogo.")


if __name__ == "__main__":
    main()