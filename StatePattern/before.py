from enum import Enum

class TransportMode(Enum):
    WALKING="walking"
    BIKE="bike"
    TRAIN="train"

class TransportService:
    def __init__(self,transport_mode:TransportMode):
        self.__transport_mode=transport_mode
    
    def set_transport(self,new_transport_mode:TransportMode):
        self.__transport_mode=new_transport_mode
    
    def eta(self):
        if self.__transport_mode==TransportMode.WALKING:
            print("walking takes 29 min")
        if self.__transport_mode==TransportMode.BIKE:
            print("walking takes 12 min")
        if self.__transport_mode==TransportMode.TRAIN:
            print("walking takes 8 min")
    
    def directions(self):
            if self.__transport_mode==TransportMode.WALKING:
                print("take left then right")
            if self.__transport_mode==TransportMode.BIKE:
                print("move to  the flyover")
            if self.__transport_mode==TransportMode.TRAIN:
                print("just sit in the train ")