from abc import ABC,abstractmethod

class Food(ABC):
    def prepare(self):
        pass

class PaneerTikka(Food):
    def prepare(self):
        print("Paneer Tikka is preparing")

class ButterChicken(Food):
    def prepare(self):
        print("ButterChicken is preparing")

class GulabJamun(Food):
    def prepare(self):
        print("GulabJamun is preparing")


class Meduvada(Food):
    def prepare(self):
        print("Meduvada is preparing")
        
class Dosa(Food):
    def prepare(self):
        print("Dosa is preparing")        

class Payasam(Food):
    def prepare(self):
        print("Payasam is preparing")  

class SpringRoll(Food):
    def prepare(self):
        print("SpringRoll is preparing")


class FriedRice(Food):
    def prepare(self):
        print("FriedRice is preparing")
        
class FortuneCookie(Food):
    def prepare(self):
        print("FortuneCookie is preparing")
        
        


class RestaurantService:
    def create_meal(self,cruisine_type:str):
        if cruisine_type=="North":
            starter=PaneerTikka()
            main_course=ButterChicken()
            dessert=GulabJamun()
        elif cruisine_type=="South":
            starter=Meduvada()
            main_course=Dosa()
            dessert=Payasam()
        elif cruisine_type=="North":
            starter=SpringRoll()
            main_course=FriedRice()
            dessert=FortuneCookie()
        else:
            print("no thing")
            
        starter.prepare()
        main_course.prepare()
        dessert.prepare()

service=RestaurantService()
service.create_meal("North")