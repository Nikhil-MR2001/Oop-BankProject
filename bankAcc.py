class BalanceException(Exception):
    print(f"Unsufficient Balance.")

class BankAccount:
    def __init__(self, intialdeposit, Accname):
        self.name = Accname
        self.balance = intialdeposit
        print(f"{Accname} has been created with a balance of ${intialdeposit:.2f}")

    def get_balance(self):
        print(f"\n The current balance of {self.name} is ${self.balance:.2f}")


    def deposit(self, amount):
        self.balance = self.balance  + amount
        print("\nSuccussfully deposited ✅.!!!!!!")
        print(f"You have successfully deposited ${amount} on '{self.name}' Account🏦. Your new balance is ${self.balance:.2f}.")


    # to check the amount that needed to be withdrawed is in the account or not
    def viableTrans(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌ Unsufficient Balance. you only got {self.balance} in your bank account")
        
    def withdraw(self, amount):
        try:
            self.viableTrans(amount)
            self.balance = self.balance - amount
            print(f"\n Withrawing from '{self.name}' Account Completed Successfully...✅✅✅")
            self.get_balance()
        except BalanceException as e:
            print(e)

    
    def transfer(self, amount, rec_acc):
        try:
            self.viableTrans(amount)
            self.withdraw(amount)
            self.get_balance()
            rec_acc.deposit(amount)
            print(f"Transfer of 💸${amount:.2f} from {self.name} ➡️ {rec_acc.name} completed successfully.")
            print(f"{self.name} new balance is ${self.balance:.2f}.")
        except BalanceException as e:
            print(e)


# 
class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        self.get_balance()
        print(f"Rupees 💸 '{amount}' with interest of {(amount * 1.05) - amount} has been credited in 🤵‍♂️{self.name}'s Account")


class SavingsAcc(InterestRewardAcc):
    def __init__(self, intialdeposit, Accname):
        super().__init__(intialdeposit, Accname)
        self.Withdrawfee = 5

    def withdraw(self, amount):
        try:
            print("\n\n\n initializing-----------------------withdrawel -------------------")
            self.viableTrans(amount=amount+self.Withdrawfee)
            self.balance -= amount+self.Withdrawfee
            self.get_balance()
            print("\n\n\n withdrawel-----------------------completed -------------------")
            print(f"\n Amount of 💸{amount} has been withdrawed from '{self.name}' Account successfully. \n Your Current bal🏦 : {self.balance}")
            
        except BalanceException as e:
            print(e)
        
