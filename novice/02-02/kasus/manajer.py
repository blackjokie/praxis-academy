from pegawai import *

class Manajer(Pegawai):
    def __init__(self, nama):
        Pegawai.__init__(self, nama, 500000)
        
    def kerja(self):
        print(self.nama, "Pengawas Pegawai")