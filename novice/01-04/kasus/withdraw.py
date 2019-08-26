class Withdraw(ATMMachine):
    def __init__(self, withdraw=0):
        self.withdraw = withdraw

    def setWithdraw(self, w):
        self.withdraw = w

    def getWithdraw(self):
        return self.setWithdraw()