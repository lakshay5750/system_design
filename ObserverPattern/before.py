class PhoneDisplay:
    def update(self,new_temp):
        print(f"Phone display temperature: {new_temp}")

 

class WeatherStation:
    def __init__(self,temperature:float):
        self.__temperature=temperature
        self.__phone_station=PhoneDisplay()
    
    def update(self,new_temp):
        self.__temperature=new_temp

    def notify(self):
        self.__phone_station.update(self.__temperature)
        
    
    
ws=WeatherStation(35)
ws.notify()
ws.update(90.12)
ws.notify()