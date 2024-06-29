from tabulate import tabulate
from appointment import Appointment

class Dokter:
    def __init__(self, nama, spesialis, jadwal):
        self.nama = nama
        self.spesialis = spesialis
        self.jadwal = jadwal
        self.appointments_head = None
        self.appointments_tail = None

    def edit_data(self, target, changes):
        if target == 0:
            self.nama = changes
        elif target == 1:
            self.spesialis = changes
        elif target == 2:
            self.jadwal = changes
    
    def enqueue_appointment(self, appointment: Appointment):
        if self.appointments_head is None:
            self.appointments_head = appointment
            appointment.next = self.appointments_head
            appointment.prev = self.appointments_head
            self.appointments_tail = self.appointments_head
        else:
            self.appointments_head.prev = appointment
            self.appointments_tail.next = appointment
            appointment.next = self.appointments_head
            appointment.prev = self.appointments_tail
            self.appointments_tail = self.appointments_tail.next
        return True

    def dequeue_appointment(self) -> bool:
        if self.appointments_head is None:
            return False
        if self.appointments_head == self.appointments_tail:
            self.appointments_head = None
            self.appointments_tail = None
        else:
            self.appointments_head.prev.next = self.appointments_head.next
            self.appointments_head.next.prev = self.appointments_head.prev
            self.appointments_head = self.appointments_head.next
            self.appointments_tail.next = self.appointments_head
        return True
    
    def cancel_appointment(self, target_username) -> bool:
        if self.appointments_head is None:
            return False
        temp = self.appointments_head
        while True:
            if temp.username_pasien == target_username:
                if temp == self.appointments_head:
                    if temp.next == temp:
                        self.appointments_head = None
                        self.appointments_tail = None
                    else:
                        self.appointments_head = temp.next
                        self.appointments_head.prev = self.appointments_tail
                        self.appointments_tail.next = self.appointments_head
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev   
                return True
            temp = temp.next
            if temp == self.appointments_head:
                break
        return False

    def appointment(self):
        return self.appointments_head

# class DokterList:
#     def __init__(self):
#         self.head = None
#         self.load_data()

#     def save_data(self):
#         with open('doctors_data.txt', 'w') as file:
#             current = self.head
#             while current:
#                 file.write(f"{current.nama}|{current.spesialis}|{current.jadwal}\n")
#                 current = current.next

#     def load_data(self):
#         if os.path.exists('doctors_data.txt'):
#             with open('doctors_data.txt', 'r') as file:
#                 for line in file:
#                     nama, spesialis, jadwal = line.strip().split('|')
#                     self.tambah_dokter_dari_data(nama, spesialis, jadwal)

#     def tambah_dokter_dari_data(self, nama, spesialis, jadwal):
#         new_dokter = Dokter(nama, spesialis, jadwal)
#         if not self.head:
#             self.head = new_dokter
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_dokter
#             new_dokter.prev = current

#     def tambah_dokter(self):
#         nama = input("Masukkan nama: ")
#         spesialis = input("Masukkan spesialis: ")
#         jadwal = input("Masukkan jadwal: ")
#         new_dokter = Dokter(nama, spesialis, jadwal)
#         if not self.head:
#             self.head = new_dokter
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_dokter
#             new_dokter.prev = current
#         self.save_data()

#     def print_list(self):
#         current = self.head
#         if not current:
#             print("List dokter kosong.")
#             return

#         doctors = []
#         while current:
#             doctors.append([current.nama, current.spesialis, current.jadwal])
#             current = current.next
#         print(tabulate(doctors, headers=["Nama", "Spesialis", "Jadwal"], tablefmt="fancy_grid"))

#     def hapus_dokter(self, nama):
#         current = self.head
#         while current:
#             if current.nama == nama:
#                 if current.prev:
#                     current.prev.next = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 if current == self.head:  # If head needs to be removed
#                     self.head = current.next
#                 print(f"Dokter {nama} berhasil dihapus.")
#                 self.save_data()
#                 return
#             current = current.next
#         print(f"Dokter {nama} tidak ditemukan.")

#     def cari_dokter(self, nama):
#         current = self.head
#         found = False
#         doctors = []
#         while current:
#             if nama.lower() in current.nama.lower():
#                 doctors.append([current.nama, current.spesialis, current.jadwal])
#                 found = True
#             current = current.next
#         if found:
#             print(tabulate(doctors, headers=["Nama", "Spesialis", "Jadwal"], tablefmt="fancy_grid"))
#         else:
#             print(f"Dokter dengan nama mengandung '{nama}' tidak ditemukan.")

#     def edit_dokter(self, nama):
#         current = self.head
#         while current:
#             if nama.lower() in current.nama.lower():
#                 print(f"Ditemukan: Nama: {current.nama}, Spesialis: {current.spesialis}, Jadwal: {current.jadwal}")
#                 print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
#                 new_nama = input(f"Nama ({current.nama}): ")
#                 new_spesialis = input(f"Spesialis ({current.spesialis}): ")
#                 new_jadwal = input(f"Jadwal ({current.jadwal}): ")
#                 if new_nama:
#                     current.nama = new_nama
#                 if new_spesialis:
#                     current.spesialis = new_spesialis
#                 if new_jadwal:
#                     current.jadwal = new_jadwal
#                 print("Data dokter berhasil diperbarui.")
#                 self.save_data()
#                 return
#             current = current.next
#         print(f"Dokter dengan nama '{nama}' tidak ditemukan.")

# def main_menu():
#     list_dokter = DokterList()
#     while True:
#         print("\nMenu:")
#         print("1. Tambah dokter")
#         print("2. Tampilkan daftar dokter")
#         print("3. Cari dokter")
#         print("4. Hapus dokter")
#         print("5. Edit dokter")
#         print("6. Keluar")
#         choice = input("Pilih menu: ")

#         if choice == '1':
#             list_dokter.tambah_dokter()
#         elif choice == '2':
#             list_dokter.print_list()
#         elif choice == '3':
#             nama = input("Masukkan nama dokter yang dicari: ")
#             list_dokter.cari_dokter(nama)
#         elif choice == '4':
#             nama = input("Masukkan nama dokter yang akan dihapus: ")
#             list_dokter.hapus_dokter(nama)
#         elif choice == '5':
#             nama = input("Masukkan nama dokter yang akan diedit: ")
#             list_dokter.edit_dokter(nama)
#         elif choice == '6':
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     main_menu()