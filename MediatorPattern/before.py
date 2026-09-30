class Airplane:
    def __init__(self,flight_number:str):
        self.__flight_number=flight_number
    
    def send_message(self,msg:str,airplane:'Airplane'):
        print(f"{self.__flight_number} is sending {msg} to the flight {self.get_flight_number()}")
    
    def get_flight_number(self):
        return self.__flight_number
    

spicejet=Airplane('spicejet-937')
indigo=Airplane('indigo-773')
indigo.send_message("landing on the runway",spicejet)