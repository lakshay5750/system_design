from abc import ABC , abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount:int):
        pass
class CreditCard(PaymentMethod):
    def pay(self,amount:int):
        return f"{amount} is done by the creditcard"
class UPI(PaymentMethod):
    def pay(self,amount:int):
        return f"{amount} is done by the UPI"
class RAZORPAY(PaymentMethod):
    def pay(self,amount:int):
        return f"{amount} is done by the RAZORPAY"
    

class PaymentProcessor:
    def process_payment(self,method:PaymentMethod,amount:int):
        print(method.pay(amount))

credit=CreditCard()
proc=PaymentProcessor()
proc.process_payment(credit,500000)