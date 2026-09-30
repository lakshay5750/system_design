from abc import ABC ,abstractmethod

class Food(ABC):
    def prepare(self):
        pass
    
class Pizza(Food):
    def prepare(self):
        print("pizza is preparing")

class Burger(Food):
    def prepare(self):
        print("burger is preparing")
        

class RestaurantService:
    def create_order(self,order:str):
        if order=="Pizza":
            f=Pizza()
            f.prepare()
            return f
        elif order=="Burger":
            f=Burger
            f.prepare()
            return f
        else:
            print("not available")

service=RestaurantService()
service.create_order("Pizza")

        