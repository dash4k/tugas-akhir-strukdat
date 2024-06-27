import os
import string
from account import DataAccount


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def ask_int(string: string) -> int:
    while True:
        try:
            choice = int(input(string))
            return choice
        except ValueError:
            continue


def true_false() -> bool:
    choice = input("\nY / N:   ")
    return True if choice in ["y", "Y"] else False



def print_header(string: string):
    width = len(string) + 4 
    print("╔" + "═" * (width) + "╗")
    print(f"║  {string}  ║")
    print("╚" + "═" * (width) + "╝")


def transpose_list(target_list: list) -> list:
    real_target = []
    for items in target_list:
        real_target.append([items])
    return list(map(list, zip(*real_target)))