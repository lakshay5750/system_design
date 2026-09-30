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


class Factory:
    @staticmethod
    def create_food(food_type:str)->Food:
        if food_type=="pizza":
            return Pizza()
        elif food_type=="burger":
            return Burger()
        else:
            return None
        
class RestaurantService:
    def create_order(self,food_type:str):
        f=Factory.create_food(food_type)
        if f is None:
            print("No order is placed")
        f.prepare()
        return f


service=RestaurantService()
service.create_order("pizza")