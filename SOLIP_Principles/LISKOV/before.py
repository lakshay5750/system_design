from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,balance):
        self.balance=balance
        
    @abstractmethod
    def withdrawn(self,amount):
        pass
    
    @abstractmethod
    def deposit(self,amount):
        pass
    
class Saving(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdrawn(self, amount):
        if amount>self.balance:
            print("Not enough balance")
        else:
            self.balance-=amount
            print(f"amount is withdrwan successfully remailing is {self.balance}")
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"amount is deposited successfurlly amount is {self.balance}")

class FD(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdrawn(self, amount):
        Exception("AMOUNT cannot be withdrawn")
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"amount is deposited successfurlly amount is {self.__balance}")
        
saving=Saving(50000)
saving.deposit(10000)