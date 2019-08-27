class Pegawai:
    def __init__(self, nama, gaji = 0):
        self.nama = nama
        self.gaji = gaji
    
    def tunjangan(self, persen):
        self.gaji = self.gaji + (self.gaji * persen)
    
    def kerja(self):
        print ("Pekerjaannya adalah", self.nama)
    
    def __repr__(self):
        return "<Pegawai: nama = %s, gaji = %s>" %(self.nama, self.gaji)
