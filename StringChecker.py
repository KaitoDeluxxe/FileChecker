from difflib import SequenceMatcher
from colorama import Fore,Style

def similar(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()*100

def main ():
    print(f"{Fore.LIGHTWHITE_EX}String Compare and Checker")
    x = input(f"Enter First String :{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} ")
    y = input(f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}Enter Second String :{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} ")
    text1 = x.strip()
    text2 = y.strip()
    if text1 == text2:
        print(f"{Fore.LIGHTGREEN_EX}[INFO]{Style.RESET_ALL}The string is the same")
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL}Similarity :{Fore.CYAN}", end=" ")
        print(similar(text1,text2), "%")
    else:
        print(f"{Fore.LIGHTRED_EX}[INFO]{Style.RESET_ALL} The string is not the same")
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Similarity :{Fore.CYAN}", end=" ")
        print("%.2f"%similar(text1, text2) ,"%")

if __name__== "__main__":
    main()
