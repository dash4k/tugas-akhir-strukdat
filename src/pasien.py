from appointment import Appointment


class Pasien:
    def __init__(self, nama, alamat_rumah, tipe_pembayaran, umur) -> None:
        self.nama = nama
        self.alamat = alamat_rumah
        self.tipe_pembayaran = tipe_pembayaran
        self.umur = umur
        self.appointments_head = None
        self.appointments_tail = None
    
    def edit_data(self, target, changes):
        if target == 0:
            self.nama = changes
        elif target == 1:
            self.alamat = changes
        elif target == 2:
            self.tipe_pembayaran = changes
        elif target == 3: 
            self.umur = changes
    
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
            if temp.username_dokter == target_username:
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