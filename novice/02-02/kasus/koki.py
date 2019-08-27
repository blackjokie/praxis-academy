from pegawai import *

class Koki(Pegawai):
    def __init__(self, nama):
        Pegawai.__init__(self, nama, 100000)
        
    def kerja(self):
        print(self.nama, "Membuat Makanan")