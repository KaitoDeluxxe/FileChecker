from colorama import Fore,Style

def main():
    print(f"{Fore.LIGHTWHITE_EX}String and Hashes Calculator{Style.RESET_ALL}")
    x = input(f"{Fore.LIGHTWHITE_EX}Enter String : {Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}{len(x.strip())}{Style.RESET_ALL}")
    hashes = {"MD5":32,"SHA1":40,"SHA224":56,"SHA256":64,"SHA384":96,"SHA512":128}
    for hash,digit in hashes.items():
        print((f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} {Fore.CYAN}{hash}{Style.RESET_ALL} hash is {Fore.GREEN}{digit}{Style.RESET_ALL} digits"))

if __name__ == "__main__":
    main()
