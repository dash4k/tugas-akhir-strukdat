import pickle
import os

from appointment import Appointment


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
            account.prev = self.head
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
        found = False
        temp = self.head
        while temp:
            if temp.type == 2:
                doctor_info = [temp.username, temp.data.nama, temp.data.spesialis, temp.data.jadwal]
                doctors.append(doctor_info)
                found = True
            temp = temp.next
            if temp == self.head:
                break
        return doctors if found else False
    
    def list_pasien(self) -> list:
        patients = []
        found = False
        temp = self.head
        while temp:
            if temp.type == 1:
                patient_info = [temp.username, temp.data.nama, temp.data.alamat, temp.data.tipe_pembayaran, temp.data.umur]
                patients.append(patient_info)
                found = True
            temp = temp.next
            if temp == self.head:
                break
        return patients if found else False

    def list_appointment(self, username) -> list:
        appointment = []
        temp = self.head
        while temp:
            if temp.username == username:
                pointer = temp.data.appointment()
                break
            temp = temp.next
            if temp == self.head:
                return False
        if pointer is None: 
            return False
        while pointer:
            appointment_info = [pointer.username_pasien, pointer.nama_dijanji, pointer.waktu]
            appointment.append(appointment_info)
            pointer = pointer.next
            if pointer == temp.data.appointment():
                break
        return appointment
    
    def return_data(self, username, type) -> list:
        temp = self.head
        while temp:
            if temp.username == username:
                if type == 1:
                    return [temp.username, temp.data.nama, temp.data.alamat, temp.data.tipe_pembayaran, temp.data.umur]
                elif type == 2:
                    return [temp.username, temp.data.nama, temp.data.spesialis, temp.data.jadwal]
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def return_account(self, username):
        temp = self.head
        index = 0
        while temp:
            if temp.username == username:
                return temp
            temp = temp.next
            index += 1
            if temp == self.head:
                return False
    
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
    
    def change_username(self, old_username, new_username, password) -> bool:
        if old_username == new_username:
            return False
        temp = self.head
        while temp:
            if temp.username == old_username and temp.password == password:
                break
            temp = temp.next
            if temp == self.head:
                return False
        temp.username = new_username
        return True
    
    def change_password(self, username, new_password, old_password) -> bool:
        temp = self.head
        while temp:
            if temp.username == username and temp.password == old_password:
                break
            temp = temp.next
            if temp == self.head:
                return False
        temp.password = new_password
        return True
    
    def enqueue_appointment(self, username_dokter, username_pasien, waktu) -> bool:
        data_dokter = self.return_account(username_dokter)
        data_pasien = self.return_account(username_pasien)
        appointment_dokter = Appointment(data_dokter.username, data_pasien.username, data_pasien.data.nama, waktu)
        appointment_pasien = Appointment(data_dokter.username, data_pasien.username, data_dokter.data.nama, waktu)
        dokter_found = False
        pasien_found = False
        temp = self.head
        while temp:
            if temp.username == username_dokter:
                if not temp.data.enqueue_appointment(appointment_dokter):
                    return False
                dokter_found = True
            elif temp.username == username_pasien:
                if not temp.data.enqueue_appointment(appointment_pasien):
                    return False
                pasien_found = True
            temp = temp.next
            if temp == self.head:
                break
        return True if (pasien_found and dokter_found) else False
    
    def dequeue_appointment(self, username_dokter, username_pasien) -> bool:
        dokter_found = False
        pasien_found = False
        temp = self.head
        while temp:
            if temp.username == username_dokter:
                if not temp.data.dequeue_appointment():
                    return False
                dokter_found = True
            elif temp.username == username_pasien:
                if not temp.data.dequeue_appointment():
                    return False
                pasien_found = True
            temp = temp.next
            if temp == self.head:
                break
        return True if (pasien_found and dokter_found) else False
    
    def cancel_appointment(self, username_dokter, username_pasien) -> bool:
        dokter_found = False
        pasien_found = False
        temp = self.head
        while temp:
            if temp.username == username_dokter:
                if not temp.data.cancel_appointment(username_pasien):
                    return False
                dokter_found = True
            elif temp.username == username_pasien:
                if not temp.data.cancel_appointment(username_dokter):
                    return False
                pasien_found = True
            temp = temp.next
            if temp == self.head:
                break
        return True if pasien_found and dokter_found else False
    
    def view_appointment(self, username) -> bool:
        temp = self.head
        while temp:
            if temp.username == username:
                return temp.data.appointment()
            temp = temp.next
            if temp == self.head:
                break
        return False

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