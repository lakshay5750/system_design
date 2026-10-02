from abc import ABC,abstractmethod

class Beverage(ABC):
    @abstractmethod
    def description(self)->str:
        pass
    @abstractmethod
    def cost(self)->int:
        pass



class Coffee(Beverage):
    def description(self)->str:
        return "Plain coffee"

    def cost(self)->int:
        return 30
    

class AddOnDecorator(Beverage):
    def __init__(self,coffee:'Coffee'):
        self.__coffee=coffee
    @abstractmethod
    def description(self):
        
        pass
    @abstractmethod
    def cost(self):
        pass


class MilkDecorator(AddOnDecorator):
    def __init__(self,coffee:'Coffee'):
        self.__coffee=coffee       
    def description(self):
        return self.__coffee.description() + ", Milk"
    
    def cost(self):
        return self.__coffee.cost()+ 20

class SugarDecorator(AddOnDecorator):
    def __init__(self,coffee:'Coffee'):
        self.__coffee=coffee
    def description(self):
        return self.__coffee.description()+" , Sugar"
    
    def cost(self):
        return self.__coffee.cost()+ 5


coffee=Coffee()
coffeewithMilk=MilkDecorator(coffee)
print(coffeewithMilk.description())
print(coffeewithMilk.cost())