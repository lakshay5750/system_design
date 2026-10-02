from abc import ABC,abstractmethod

class Beverage(ABC):
    def description(self)->str:
        pass
    
    def cost(self)->int:
        pass



class Coffee(Beverage):
    def description(self)->str:
        return "Plain coffee"

    def cost(self)->int:
        return 30

class CoffeeWithMilk(Beverage):
    def description(self)->str:
        return "Plain coffee with milk"

    def cost(self)->int:
        return 50

class CoffeeWithMilkSugar(Beverage):
    def description(self)->str:
        return "Plain coffee with milk and sugar"

    def cost(self)->int:
        return 80
    

coffee=Coffee()
description=coffee.description()
price=coffee.cost()
print(description,price)
print("------------------------")
coffeemilk=CoffeeWithMilk()
description1=coffeemilk.description()
price1=coffeemilk.cost()
print(description1,price1)