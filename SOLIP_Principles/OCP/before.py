class PaymentProcessor:
    def pay(self,method:str,amount:int):
        if method=='UPI':
            return f"{method} transaction is going to taking place of amount {amount}"
        if method=='CREDITCARD':
                    return f"{method} transaction is going to taking place of amount {amount}"
        if method=='DEBITCARD':
                    return f"{method} transaction is going to taking place of amount {amount}"
                
py=PaymentProcessor()
print(py.pay('CREDITCARD',50000000))