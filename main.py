import requests
import os
from colorama import Fore, Style, init

#first tool i wrote
#just a simple tool created by gr1m ethical a student beginner
#im just wrting this tool to improve my self experiment/taught in automation related on cybersecurity

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

domain = input("Enter Domain:")



def scan(domain):
    if "." not in domain:
        print(f"{Fore.RED}[{Fore.WHITE}-{Fore.RED}] {Fore.WHITE}Invalid Domain")
        exit()
    elif domain.startswith("http://"):
        domain = domain.replace("http://", "", 1)
    elif domain.startswith("https://"):
        domain = domain.replace("https://", "", 1)
    elif domain.endswith("/"):
        domain = domain[:-1]

    ask = input(f"{Fore.WHITE}You want a custom wordlist? (Y/N=default):"+Fore.YELLOW).upper()
    #SUBFINDER

    if ask == "Y":
        wordlist = input(f"{Fore.WHITE}Enter your wordlist:{Fore.YELLOW} ")
        if wordlist.endswith(".txt"):
            total = 0
            count = 0
            try:
                with open(wordlist, "r", encoding="utf-8") as words:

                    for item in words:
                        total += 1
                        url = f'https://' + item.strip() + "." + domain
                        print(f"{Fore.LIGHTBLUE_EX}[...] Scanning {url} {Fore.RED}| {Fore.GREEN}Found: {Fore.YELLOW}{count} {Fore.RED}| {Fore.GREEN}Checked: {Fore.YELLOW}{total}", end="\r", flush=True)
                        try:
                            r = requests.get(url, timeout=3)
                            stats = r.status_code
                            if stats < 400:
                                print(' ' * 120, end='\r')
                                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.GREEN}FOUND {url}")
                                count += 1
                            else:
                                print(f"{Fore.RED}[{Fore.WHITE}-{Fore.RED}]{Fore.RED} NOT FOUND {url}")

                        except requests.RequestException:
                           pass
                    print(f"{Fore.GREEN}[+] Total Found:{Fore.YELLOW}",count)

            except FileNotFoundError:
                print("wordlists file not found. Please check the file location.")
        else:
            print("Invalid File")
    else:
        with open("subdomains.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            counts = len(lines)
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.GREEN}Loaded {Fore.YELLOW}{counts} {Fore.GREEN}list")
        total = 0
        count = 0
        try:
            with open("subdomains.txt", "r", encoding="utf-8") as words:
                for item in words:
                    total += 1
                    url = f'https://' + item.strip() + "." + domain
                    print(f"{Fore.LIGHTBLUE_EX}[...] Scanning {url} {Fore.RED}| {Fore.GREEN}Found: {Fore.YELLOW}{count} {Fore.RED}| {Fore.GREEN}Checked: {Fore.YELLOW}{total}",
                        end="\r", flush=True)
                    try:
                        r = requests.get(url, timeout=3)
                        stats = r.status_code
                        if stats < 400:
                            print(' ' * 120, end='\r')
                            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.GREEN}FOUND {url}")
                            count += 1
                        else:
                            print(f"{Fore.RED}[{Fore.WHITE}-{Fore.RED}]{Fore.RED} NOT FOUND {url}")

                    except requests.RequestException:
                        pass
                print(f"{Fore.GREEN}[+] Total Found:{Fore.YELLOW}", count)

        except FileNotFoundError:
            print("wordlists file not found. Please check the file location.")

try:
    scan(domain)
except KeyboardInterrupt:
    print("\n[!] Scan interrupted by you. Goodbye!")

