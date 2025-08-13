# Create Account class with 2 attributes balance and account no.
# Create methods for debit,credit and printing the balace

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc_num = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs:",amount,"was debited from your account")
        print("Your current balance is ",self.balance)
    
    def credit(self,amount):
        self.balance += amount
        print("Rs:",amount,"was credited to your account")
        print("Your current balance is ",self.balance)
        
    def get_balance(self):
        return self.balance


ac1 = Account(18000,1101)
print(ac1.get_balance())
print(ac1.acc_num)
ac1.debit(2000)
ac1.credit(1000)
