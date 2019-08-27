from koki import *

class PizzaRobot(Koki):
    def __init__(self, nama):
        Koki.__init__(self, nama)
        
    def kerja(self):
        print(self.nama, "Membuat Pizza")