from account import DataAccount
from appointment import Appointment


class Pasien:
    def __init__(self, nama, alamat_rumah, tipe_pembayaran, umur) -> None:
        self.nama = nama
        self.alamat = alamat_rumah
        self.tipe_pembayaran = tipe_pembayaran
        self.umur = umur
        self.appointments = []
    
    def edit_data(self, target, changes):
        if target == 0:
            self.nama = changes
        elif target == 1:
            self.alamat = changes
        elif target == 2:
            self.tipe_pembayaran = changes
        elif target == 3: 
            self.umur = changes
    
    def add_appointment(self, doctor_name, date_time, database: DataAccount) -> bool:
        appointment = Appointment(self.nama, doctor_name, date_time)
        self.appointments.append(appointment)
        temp = database.head
        while temp:
            if temp.data.nama == doctor_name:
                break
            temp = temp.next
            if temp == self.head:
                return False
        temp.data.appointment.apped(appointment)
        return True