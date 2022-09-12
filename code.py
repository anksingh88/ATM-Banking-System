import random
import time
import datetime
print("PLEASE INSERT YOUR CARD")
time.sleep(1)   #for card processing
input("Press ENTER To Continue.......")
print("  ")
print("\n\n\t\t\t NATIONAL bANK ATM 24/7\n")
print("-----------------------------------------------------")
class Account:
    # Construct an Account object
    def __init__(self, id, balance = 0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
 
    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def getAnnualInterestRate(self):
        return self.annualInterestRate
 
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
 
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
def main():
   # Creating accounts
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)
       # ATM Processes
   while True:
 
       # Reading id from user
       id = int(input("\nEnter account pin: "))
 
       # Loop till id is valid
       while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id.. Re-enter: "))
 
       # Iterating over account session
       while True:
 
           # Printing menu
           #print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
           print("\n\n\t\t\t 1: View Balance \n\t\t\t 2: Withdraw \n\t\t\t 3: Deposit \n\t\t\t 5: Pin change \n\t\t\t 4: Exit\n")
 
           # Reading selection
           selection = int(input("\nEnter your selection: "))
 
           # Getting account object
           for acc in accounts:
               # Comparing account id
               if acc.getId() == id:
                   accountObj = acc
                   break
           # View Balance
           if selection == 1:
               # Printing balance
               print(accountObj.getBalance())
               
           # change pin
           elif selection == 5:
               changepin=int(input("enter the new pin  :  "))
               id=changepin
               print("Account pin is updated")

           # Withdraw
           elif selection == 2:
               # Reading amount
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
               if ver_withdraw == "Yes":
                   print("Verify withdraw")
               else:
                   break
 
               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()))
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()))
                    print("\nPlease make a deposit.");
               # Deposit
           elif selection == 3:
               # Reading amount
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
               if ver_deposit == "Yes":
                  # Calling deposit method
                  accountObj.deposit(amt);
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()))
               else:
                   break
 
           elif selection == 4:
               print("\t\t Transaction is now complete.")
               print("\t\t Transaction number: ", random.randint(10000, 1000000))
               print("\t\t Current Interest Rate: ", accountObj.annualInterestRate)
               print("\t\t Monthly Interest Rate: ",accountObj.annualInterestRate / 12)
               x=datetime.datetime.now()
               print("\t\t date  :",x)
               print("\t\t Thanks for choosing us as your bank")
               time.sleep(3)
               exit()
 
           # Any other choice
           else:
               print("nThat's an invalid choice.")
# Main function
main()








                    

