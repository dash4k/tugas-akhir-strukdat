from dokter import Dokter
from util import ask_int, clear, print_header, true_false, transpose_list
from account import Account, DataAccount
from pasien import Pasien
from tabulate import tabulate


header_akun_admin = ["Username", "Password", "Account Type"]
header_manajemen_pasien = ["Index", "Username", "Nama", "Alamat", "Tipe Pembayaran", "Umur"]
header_cari_pasien = ["Username", "Nama", "Alamat", "Tipe Pembayaran", "Umur"]
header_manajemen_dokter = ["Index", "Username", "Nama", "Spesialis", "Jadwal"]
header_cari_dokter = ["Username", "Nama", "Spesialis", "Jadwal"]
header_edit_pasien = ["Nama", "Alamat", "Tipe Pembayaran", "Umur"]
header_edit_dokter = ["Nama", "Spesialis", "Jadwal"]
flag1 = flag2 = flag3 = flag4 = True
data = DataAccount()
admin = Account("admin", "admin", 3)
data.add_account(None, admin)
while flag1:
    clear()
    print("╔════════════════════════════╗")
    print("║    Manajemen Rumah Sakit   ║")
    print("║           Login            ║")
    print("║                            ║")
    print("║   1. Login                 ║")
    print("║   2. Sign Up               ║")
    print("║   3. Exit                  ║")
    print("║                            ║")
    print("╚════════════════════════════╝")
    choice = ask_int("Choice: ")
    if choice == 1:
        clear()
        print_header("Log In")
        username = input("\nUsername: ")
        password = input("Passowrd: ")
        user_data = data.login(username, password)
        if not user_data:
            input("\n\nIncorrect Username or Password!\n\nPress enter to continue........")
            continue
        else:
            if user_data.type == 1:
                while flag2:
                    clear()
                    print(f"Welcome {user_data.data.nama}!")
                    print("╔════════════════════════════╗")
                    print("║                            ║")
                    print("║         Main Menu          ║")
                    print("║                            ║")
                    print("║   1. Buat Janji            ║")
                    print("║   2. Batalkan Janji        ║")
                    print("║   3. Lihat Janji           ║")
                    print("║   4. Pengaturan            ║")
                    print("║   5. Back                  ║")
                    print("║                            ║")
                    print("╚════════════════════════════╝")
                    choice1 = ask_int("Choice: ")
                    if choice1 == 1:
                        # clear()
                        # print(f"\tReservation\n")
                        # print(tabulate(data.list_dokter()))
                        continue
                    elif choice1 == 2:
                        continue
                    elif choice1 == 3:
                        continue
                    elif choice1 == 4:
                        continue
                    elif choice1 == 5:
                        break
            elif user_data.type == 2:
                while flag2:
                    clear()
                    print(f"Welcome {user_data.data.nama}!")
                    print("╔════════════════════════════╗")
                    print("║                            ║")
                    print("║         Main Menu          ║")
                    print("║                            ║")
                    print("║   1. Selesaikan Janji      ║")
                    print("║   2. Batalkan Janji        ║")
                    print("║   3. Lihat Janji           ║")
                    print("║   4. Pengaturan            ║")
                    print("║   5. Back                  ║")
                    print("║                            ║")
                    print("╚════════════════════════════╝")
                    choice1 = ask_int("Choice: ")
                    if choice1 == 1:
                        continue
                    elif choice1 == 2:
                        continue
                    elif choice1 == 3:
                        continue
                    elif choice1 == 4:
                        continue
                    elif choice1 == 5:
                        break
            elif user_data.type == 3:
                while flag2:
                    clear()
                    print(f"Welcome {user_data.username}!")
                    print("╔════════════════════════════╗")
                    print("║                            ║")
                    print("║         Main Menu          ║")
                    print("║                            ║")
                    print("║   1. Manajemen Pasien      ║")
                    print("║   2. Manajemen Dokter      ║")
                    print("║   3. Pengaturan            ║")
                    print("║   4. Back                  ║")
                    print("║                            ║")
                    print("╚════════════════════════════╝")
                    choice1 = ask_int("Choice: ")
                    if choice1 == 1:
                        while flag3:
                            clear()
                            print("╔════════════════════════════╗")
                            print("║                            ║")
                            print("║      Manajemen Pasien      ║")
                            print("║                            ║")
                            print("║   1. Edit Data Pasien      ║")
                            print("║   2. Hapus Data Pasien     ║")
                            print("║   3. Cari Pasien           ║")
                            print("║   4. List Pasien           ║")
                            print("║   5. Back                  ║")
                            print("║                            ║")
                            print("╚════════════════════════════╝")
                            choice2 = ask_int("Choice: ")
                            if choice2 == 1:
                                clear()
                                print_header("Data Pasien")
                                target_list = data.list_pasien()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                try:
                                    print(tabulate(target_list, headers=header_manajemen_pasien, tablefmt="fancy_grid", showindex=True))
                                    target = ask_int("\nChoice: ")
                                    clear()
                                    print_header("Edit Data Pasien")
                                    transposed_list = transpose_list(target_list[target][1:])
                                    print(tabulate(transposed_list, headers=header_edit_pasien, tablefmt="fancy_grid"))
                                    print("\n(Type Anything Else to Cancel)")
                                    choice3 = input("\nChoice: ").lower()
                                    if choice3 == "nama":
                                        index_change = 0
                                    elif choice3 == "alamat":
                                        index_change = 1
                                    elif choice3 == "tipe pembayaran":
                                        index_change = 2
                                    elif choice3 == "umur":
                                        index_change = 3
                                    else:
                                        continue
                                    changes = input("Masukkan edit: ")
                                    clear()
                                    print_header("Hasil Edit Data")
                                    if not data.edit_data(index_change, changes, target_list[target][0]):
                                        print(transposed_list)
                                        input("Error...")
                                    else:
                                        target_list = data.list_pasien()
                                        transposed_list = transpose_list(target_list[target][1:])
                                        print(tabulate(transposed_list, headers=header_edit_pasien, tablefmt="fancy_grid"))
                                        input("\nPress Enter to Continue.......")
                                    continue
                                except IndexError:
                                    input("\n\nInvalid Index!\n\nPress enter to continue........")
                                    continue
                            elif choice2 == 2:
                                clear()
                                print_header("Data Pasien")
                                target_list = data.list_pasien()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                try:
                                    print(tabulate(target_list, headers=header_manajemen_pasien, tablefmt="fancy_grid", showindex=True))
                                    target = ask_int("\nChoice: ")
                                    clear()
                                    print_header("Hapus Data Pasien")
                                    transposed_list = transpose_list(target_list[target][1:])
                                    print(tabulate(transposed_list, headers=header_edit_pasien, tablefmt="fancy_grid"))
                                    if true_false():
                                        if not data.remove_account(target_list[target][0].strip()):
                                            print(transposed_list)
                                            input("Error...")
                                    clear()
                                    print_header("Data Pasien")
                                    target_list = data.list_pasien()
                                    print(tabulate(target_list, headers=header_manajemen_pasien, tablefmt="fancy_grid", showindex=True))
                                    input("\nPress Enter to Continue.......")
                                    continue
                                except IndexError:
                                    input("\n\nInvalid Index!\n\nPress enter to continue........")
                                    continue
                            elif choice2 == 3:
                                while flag4:
                                    clear()
                                    print_header("Cari Pasien")
                                    target = input("\nMasukkan Kata Kunci: ")
                                    target_list = data.find(target.lower(), 1)
                                    if not target_list:
                                        input("\n\n404 Not Found!\n\nPress enter to continue........")
                                        break
                                    print(tabulate(target_list, headers=header_cari_pasien, tablefmt="fancy_grid"))
                                    print("\nContinue?")
                                    if true_false():
                                        continue
                                    break
                            elif choice2 == 4:
                                clear()
                                print_header("Data Pasien")
                                target_list = data.list_pasien()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                print(tabulate(target_list, headers=header_manajemen_pasien, tablefmt="fancy_grid", showindex=True))
                                input("\n\nPress enter to continue........")
                                continue
                            elif choice2 == 5:
                                break
                    elif choice1 == 2:
                        while flag3:
                            clear()
                            print("╔════════════════════════════╗")
                            print("║                            ║")
                            print("║      Manajemen Dokter      ║")
                            print("║                            ║")
                            print("║   1. Tambah Data Dokter    ║")
                            print("║   2. Edit Data Dokter      ║")
                            print("║   3. Hapus Data Dokter     ║")
                            print("║   4. Cari Dokter           ║")
                            print("║   5. List Dokter           ║")
                            print("║   6. Back                  ║")
                            print("║                            ║")
                            print("╚════════════════════════════╝")
                            choice2 = ask_int("Choice: ")
                            if choice2 == 1:
                                clear()
                                print_header("Doctor Sign Up Form")
                                username = input("\nUsername: ")
                                password = input("\nPassowrd: ")
                                clear()
                                print_header("Patient Sign Up Form")
                                nama = input("\nNama Lengkap: ").title()
                                spesialis = input("\nSpesialis: ").title()
                                jadwal = input("\nJadwal: ")
                                temp_acc = Account(username, password, 2)
                                temp_dokter = Dokter(nama, spesialis, jadwal)
                                data.add_account(temp_dokter, temp_acc)
                                continue
                            elif choice2 == 2:
                                clear()
                                print_header("Data Dokter")
                                target_list = data.list_dokter()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                try:
                                    print(tabulate(target_list, headers=header_manajemen_dokter, tablefmt="fancy_grid", showindex=True))
                                    target = ask_int("\nChoice: ")
                                    clear()
                                    print_header("Edit Data Dokter")
                                    transposed_list = transpose_list(target_list[target][1:])
                                    print(tabulate(transposed_list, headers=header_edit_dokter, tablefmt="fancy_grid"))
                                    print("\n(Type Anything Else to Cancel)")
                                    choice3 = input("\nChoice: ").lower()
                                    if choice3 == "nama":
                                        index_change = 0
                                    elif choice3 == "spesialis":
                                        index_change = 1
                                    elif choice3 == "jadwal":
                                        index_change = 2
                                    else:
                                        continue
                                    changes = input("Masukkan edit: ")
                                    clear()
                                    print_header("Hasil Edit Data")
                                    if not data.edit_data(index_change, changes, target_list[target][0]):
                                        print(target_list[target][0])
                                        input("Error...")
                                    else:
                                        target_list = data.list_dokter()
                                        transposed_list = transpose_list(target_list[target][1:])
                                        print(tabulate(transposed_list, headers=header_edit_dokter, tablefmt="fancy_grid", showindex=True))
                                        input("\n\nPress enter to continue........")
                                    continue
                                except IndexError:
                                    input("\n\nInvalid Index!\n\nPress enter to continue........")
                                    continue
                            elif choice2 == 3:
                                clear()
                                print_header("Data Dokter")
                                target_list = data.list_dokter()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                try:
                                    print(tabulate(target_list, headers=header_manajemen_dokter, tablefmt="fancy_grid", showindex=True))
                                    target = ask_int("\nChoice: ")
                                    clear()
                                    print_header("Hapus Data Dokter")
                                    transposed_list = transpose_list(target_list[target][1:])
                                    print(tabulate(transposed_list, headers=header_edit_dokter, tablefmt="fancy_grid"))
                                    if true_false():
                                        if not data.remove_account(target_list[target][0].strip()):
                                            print(target_list[target][0])
                                    clear()
                                    print_header("Data Dokter")
                                    target_list = data.list_dokter()
                                    print(tabulate(target_list, headers=header_manajemen_dokter, tablefmt="fancy_grid", showindex=True))
                                    input("\nPress Enter to Continue.......")
                                    continue
                                except IndexError:
                                    input("\n\nInvalid Index!\n\nPress enter to continue........")
                                    continue
                            elif choice2 == 4:
                                while flag4:
                                    clear()
                                    print_header("Cari Dokter")
                                    target = input("\nMasukkan Kata Kunci: ")
                                    target_list = data.find(target.lower(), 2)
                                    if not target_list:
                                        input("\n\n404 Not Found!\n\nPress enter to continue........")
                                        break
                                    print(tabulate(target_list, headers=header_cari_dokter, tablefmt="fancy_grid"))
                                    print("\nContinue?")
                                    if true_false():
                                        continue
                                    break
                            elif choice2 == 5:
                                clear()
                                print_header("Data Dokter")
                                target_list = data.list_dokter()
                                if not target_list:
                                    input("\n\nThe List is Empty!\n\nPress enter to continue........")
                                    continue
                                print(tabulate(target_list, headers=header_manajemen_dokter, tablefmt="fancy_grid", showindex=True))
                                input("\n\nPress enter to continue........")
                                continue
                            elif choice2 == 6:
                                break
                    elif choice1 == 3:
                        while flag3:
                            clear()
                            print("╔════════════════════════════╗")
                            print("║                            ║")
                            print("║      Pengaturan            ║")
                            print("║                            ║")
                            print("║   1. Detail Akun           ║")
                            print("║   2. Ubah Username         ║")
                            print("║   3. Ubah Password         ║")
                            print("║   4. Back                  ║")
                            print("║                            ║")
                            print("╚════════════════════════════╝")
                            choice2 = ask_int("Choice: ")
                            if choice2 == 1:
                                detail_akun = [[user_data.username], [user_data.password], ["Admin"]]
                                transposed_list = list(map(list, zip(*detail_akun)))
                                clear()
                                print_header("Detail Akun")
                                print(tabulate(transposed_list, headers=header_akun_admin, tablefmt="fancy_grid"))
                                input("\n\nPress enter to continue........")
                                continue
                            elif choice2 == 2:
                                continue
                            elif choice2 == 3:
                                continue
                            elif choice2 == 4:
                                break
                    elif choice1 == 4:
                        break
    elif choice == 2:
        clear()
        print_header("Patient Sign Up Form")
        username = input("\nUsername: ")
        password = input("\nPassowrd: ")
        clear()
        print_header("Patient Sign Up Form")
        nama = input("\nNama Lengkap: ").title()
        alamat = input("\nAlamat: ").title()
        umur = input("\nUmur: ")
        clear()
        print_header("Patient Sign Up Form")
        print("╔════════════════════════════╗")
        print("║                            ║")
        print("║       Tipe Pembayaran      ║")
        print("║                            ║")
        print("║   1. Umum                  ║")
        print("║   2. Asuransi              ║")
        print("║   3. BPJS                  ║")
        print("║                            ║")
        print("╚════════════════════════════╝")
        choice1 = ask_int("Choice: ")
        if choice1 == 1:
            tipe = "Umum"
        elif choice1 == 2:
            tipe = "Asuransi"
        elif choice1 == 3:
            tipe = "BPJS"
        else:
            tipe = "Umum"
        temp_acc = Account(username, password, 1)
        temp_patient = Pasien(nama, alamat, tipe, umur)
        data.add_account(temp_patient, temp_acc)
        continue
    elif choice == 3:
        break
data.save_data()