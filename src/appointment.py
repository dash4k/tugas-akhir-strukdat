# Modul Class Appointment
class Appointment:
    def __init__(self, username_dokter, username_pasien, nama_dijanji, waktu) -> None:
        self.username_dokter = username_dokter
        self.username_pasien = username_pasien
        self.nama_dijanji = nama_dijanji
        self.waktu = waktu
        self.next = None
        self.prev = None