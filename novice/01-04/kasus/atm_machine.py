from balance import *
from deposit import *
from withdraw import *

class ATMMachine():
    def __init__(self, balance=0):
        self.balance = balance

    def checkBalance(self, b):
        self.balance = b

    def withdrawMoney(self):
        return self.setBalance()

    def depositMoney(self):
        return self.setBalance()

print ("=============================")
print ("Welcome to Simple ATM Machine")
print ("============================= \n")
print ("Please Select ATM Transaction \n 1. Deposit \n 2. Withdaraw \n 3. Balance Inquiry \n 4. Exit \n")

answer = input ("what would you like to do? (1,2,3,4) ")

if answer == "1": 
    
    print ("\tYour current balance is " + Balance.getBalance());
    
elif answer == "2":
    print ("Goodbye!")

elif answer == "3":
    print ("Goodbye!")

elif answer== "4":
    print ("Goodbye!")


else:
    print ("I'm sorry, that is not an option")