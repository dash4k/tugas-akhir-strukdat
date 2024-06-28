import os
from account import DataAccount


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def ask_int(str: str) -> int:
    while True:
        try:
            choice = int(input(str))
            return choice
        except ValueError:
            continue


def true_false() -> bool:
    choice = input("\nY / N:   ")
    return True if choice in ["y", "Y"] else False



def print_header(str: str):
    max_width = 86
    total_width = max_width + 4
    print("╔" + "═" * (total_width - 2) + "╗")
    print(f"║ {str.center(max_width)} ║")
    print("╚" + "═" * (total_width - 2) + "╝")


def print_jadwal(dokter: str, jadwal: str):
    max_width = 86
    total_width = max_width + 4
    print("╔" + "═" * (total_width - 2) + "╗")
    print(f"║ {dokter.center(max_width)} ║")
    print(f"║ {jadwal.center(max_width)} ║")
    print("╚" + "═" * (total_width - 2) + "╝")


def transpose_list(target_list: list) -> list:
    real_target = []
    for items in target_list:
        real_target.append([items])
    return list(map(list, zip(*real_target)))


def print_alert(str: str) -> None:
    clear()
    print_header(str)
    input("\n\nPress enter to continue...............")