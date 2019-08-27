from pegawai import *
from manajer import *
from koki import *
from pelayan import *
from pizza_bot import *
import unittest

# membuat variabel baru dgn nama "agus" dan memanggil class "PizzaRobot" dengan atribut nama "Agus" 
agus = PizzaRobot("Agus")
# menampilkan hasil variabel "agus"
print(agus)
#  
agus.kerja()
# 
agus.tunjangan(0.50)
# 
print(agus)
    
for kelas in Pegawai, Manajer, Koki, Pelayan, PizzaRobot:
    objek = kelas(kelas.__name__)
    objek.kerja()
        
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(agus.nama, "Agus")
        # self.assertTrue(agus.nama.isupper, "Agus")

if __name__ == '__main__':
    unittest.main()