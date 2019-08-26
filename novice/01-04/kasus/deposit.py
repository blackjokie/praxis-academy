class Deposit(ATMMachine):
    def __init__(self, deposit):
        self.deposit = deposit

    def setDeposit(self, d):
        self.deposit = d

    def getDeposit(self):
        return self.setDeposit()