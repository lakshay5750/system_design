from withdrawl import Withdrawl

class Saving(Withdrawl):
    def __init__(self, balance):
        super().__init__(balance)
    
    def deposit(self, amount):
        self.balance+=self.amount
        print(f"Amoutn is deposited successfully {self.balance}")
        
    def withdraw(self, amount):
            if amount>self.balance:
                print(f"Not enough balance")
                
            else:
                self.balance-=amount
                print(f"Amoutn is withdraw successfully {self.balance}")
                
            
            