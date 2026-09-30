from abc import ABC , abstractmethod
from typing import List
class AirTrafficController:
    def register_airplane(self):
        pass
    def send_message(self):
        pass

class ControlTower(AirTrafficController):
    def __init__(self):
        self.__airplanes:List[Airplane]=[]
    def register_airplane(self,new_airplane:'Airplane'):
        self.__airplanes.append(new_airplane)
        
    def send_message(self,msg:str,airplanee:'Airplane'):
        for airplane in self.__airplanes:
            airplane.recieve_message(msg,airplanee)
        

class Airplane:
    def __init__(self,flight_number:str,tower:'ControlTower'):
        self.__flight_number=flight_number
        self.__tower=tower
        self.__tower.register_airplane(self)
    
    def send_message(self,msg:str):
        self.__tower.send_message(msg,self)
        
    def get_flight_number(self)->str:
        return self.__flight_number
    
    def recieve_message(self,msg:str,who_sent:'Airplane'):
        print(f"{self.__flight_number} is sent {msg} to the flight {who_sent.get_flight_number()}")
        


tower=ControlTower()
airIndia=Airplane('air-india-245',tower)
spicejet=Airplane('spicejet-5612',tower)
indigo=Airplane('indigo-892',tower)

airIndia.send_message("i am going to landing")