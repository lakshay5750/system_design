from abc import ABC,abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Main_course(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass
    

class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self)->Starter:
        pass
    
    @abstractmethod
    def create_main_course(self)->Main_course:
        pass
    
    @abstractmethod
    def create_dessert(self)->Dessert:
        pass
    

class NorthFood(CuisineFactory):
    def create_starter(self):
        return PaneerTikka()
    def create_main_course(self):
        return ButterChicken()
    def create_dessert(self):
        return GulabJamun()
    
class SouthFood(CuisineFactory):
    def create_starter(self):
        return Meduvada()
    def create_main_course(self):
        return Dosa()
    def create_dessert(self):
        return Payasam()

class ChineseFood(CuisineFactory):
    def create_starter(self):
        return SpringRoll()
    def create_main_course(self):
        return FriedRice()
    def create_dessert(self):
        return FortuneCookie()
        

class PaneerTikka(Starter):
    def prepare(self):
        print("Paneer Tikka is preparing")

class ButterChicken(Main_course):
    def prepare(self):
        print("ButterChicken is preparing")

class GulabJamun(Dessert):
    def prepare(self):
        print("GulabJamun is preparing")


class Meduvada(Starter):
    def prepare(self):
        print("Meduvada is preparing")
        
class Dosa(Main_course):
    def prepare(self):
        print("Dosa is preparing")        

class Payasam(Dessert):
    def prepare(self):
        print("Payasam is preparing")  

class SpringRoll(Starter):
    def prepare(self):
        print("SpringRoll is preparing")


class FriedRice(Main_course):
    def prepare(self):
        print("FriedRice is preparing")
        
class FortuneCookie(Dessert):
    def prepare(self):
        print("FortuneCookie is preparing")
        
        

class RestaurantService:
    def __init__(self,factory:CuisineFactory):
        self.__factory=factory
    
    def create_meal(self):
        starter=self.__factory.create_starter()
        main_course=self.__factory.create_main_course()
        dessert=self.__factory.create_dessert()
        starter.prepare()
        main_course.prepare()
        dessert.prepare()
        
service=RestaurantService(NorthFood())
service.create_meal()
