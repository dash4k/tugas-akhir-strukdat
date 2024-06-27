import pickle
import os


class Account:
    def __init__(self, username, password, type: int) -> None:
        self.username = username
        self.password = password
        self.type = type                                                   # 1: Pasien, 2: Dokter, 3: Admin
        self.data = None
        self.next = None
        self.prev = None


class DataAccount:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.load_data()

    def add_account(self, data, account: Account) -> None:
        temp = self.head
        while temp:
            if temp.username == account.username:
                return False
            temp = temp.next
            if temp == self.head:
                break
        if self.head is None:
            self.head = account
            account.next = self.head
            account.pref = self.head
            self.tail = self.head
            self.head.data = data
        else:
            self.head.prev = account
            self.tail.next = account
            account.next = self.head
            account.prev = self.tail
            self.tail = self.tail.next
            self.tail.data = data

    def remove_account(self, target_username) -> bool:
        if self.head is None:
            return False
        temp = self.head
        while True:
            if temp.username == target_username:
                if temp == self.head:
                    if temp.next == temp:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = temp.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev   
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def login(self, username, password):
        temp = self.head
        index = 0
        while temp:
            if temp.username == username and temp.password == password:
                return temp
            temp = temp.next
            index += 1
            if temp == self.head:
                return False
    
    def list_dokter(self) -> list:
        doctors = []
        temp = self.head
        while temp:
            if temp.type == 2:
                doctor_info = [temp.username, temp.data.nama, temp.data.spesialis, temp.data.jadwal]
                doctors.append(doctor_info)
            temp = temp.next
            if temp == self.head:
                break
        return doctors
    
    def list_pasien(self) -> list:
        patients = []
        temp = self.head
        while temp:
            if temp.type == 1:
                patient_info = [temp.username, temp.data.nama, temp.data.alamat, temp.data.tipe_pembayaran, temp.data.umur]
                patients.append(patient_info)
            temp = temp.next
            if temp == self.head:
                break
        return patients
    
    def find(self, target, type) -> list:
        daftar_data = []
        temp = self.head
        found = False
        if type == 1:
            while temp:
                if temp.type == 1:
                    if target in temp.username.lower() or target in temp.data.nama.lower() or target in temp.data.alamat.lower() or target in temp.data.tipe_pembayaran.lower() or target in temp.data.umur:
                        data = [temp.username, temp.data.nama, temp.data.alamat, temp.data.tipe_pembayaran, temp.data.umur]
                        found = True
                        daftar_data.append(data)
                temp = temp.next
                if temp == self.head:
                    break
            return daftar_data if found else False
        elif type == 2:
            while temp:
                if temp.type == 2:
                    if target in temp.username.lower() or target in temp.data.nama.lower() or target in temp.data.spesialis.lower() or target in temp.data.jadwal.lower():
                        data = [temp.username, temp.data.nama, temp.data.spesialis, temp.data.jadwal]
                        found = True
                        daftar_data.append(data)
                temp = temp.next
                if temp == self.head:
                    break
            return daftar_data if found else False
    
    def edit_data(self, target, changes, username) -> bool:
        temp = self.head
        while temp:
            if temp.username == username:
                break
            temp = temp.next
            if temp == self.head:
                return False
        temp.data.edit_data(target, changes.title())
        return True
    
    def save_data(self):
        if self.head is None:
            return False
        with open("database.pkl", "wb") as file:
            temp = self.head
            while temp:
                pickle.dump(temp, file)
                temp = temp.next
                if temp == self.head:
                    return True
    
    def load_data(self):
        if not os.path.exists("database.pkl"):
            return False
        self.head = None
        self.tail = None
        with open("database.pkl", "rb") as file:
            while True:
                try:
                    account = pickle.load(file)
                    self.add_account(account.data, account)
                except EOFError:
                    return True