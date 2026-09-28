from transport_mode import TransportMode


class TransportService:
    def __init__(self,transport_mode:TransportMode):
        self.__transport_mode=transport_mode
    def set_mode(self,new_transport_mode:TransportMode):
        self.__transport_mode=new_transport_mode
    
    def eta(self):
        self.__transport_mode.eta()
    def direction(self):
        self.__transport_mode.direction()