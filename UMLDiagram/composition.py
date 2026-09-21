from typing import Optional

class Engine:
    def __init__(self,engine_type:str,horse_power:str)->None:
        self.__engine_type=engine_type
        self.__horse_power=horse_power
    def get_details(self)->str:
        return f"{self.__engine_type} Engine {self.__horse_power} hp"
    
    def start(self)->None:
        return f"{self.__engine_type} engine is started"
    

class Car:
    def __init__(self,brand:str,model:str,engine_type,horse_power):
        self.__brand=brand
        self.__model=model
        self.__engine=Engine(engine_type,horse_power)
    
    def get_car_details(self)->None:
        print(f"Car {self.__brand} Model {self.__model}")
        print(f"Engine details {self.__engine.get_details()}")
    
    def start_car(self)->None:
        self.__engine.start()
        print("Car is ready to roar")
        
if __name__=="__main__":
    car:Car=Car("roll_royce","xml25","Diesel",204)
    car.get_car_details()