from pegawai import *

class Pelayan(Pegawai):
    def __init__(self, nama):
        Pegawai.__init__(self, nama, 50000)
        
    def kerja(self):
        print(self.nama, "Melayani Customer")