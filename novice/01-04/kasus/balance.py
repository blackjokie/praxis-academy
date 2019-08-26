class Balance(ATMMachine):
    def __init__(self, balance=0):
        self.balance = balance

    def setBalance(self, b):
        self.balance = b

    def getBalance(self):
        return self.setBalance()