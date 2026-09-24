from typing import List
from observer import Observer

class WeatherStation:
    def __init__(self):
        self.__temperature=0
        self.__observer:List[Observer]=[]
    
    def update(self,new_temp):
        self.__temperature=new_temp
        self.notify()
    
    def add_observer(self,observer:Observer):
        self.__observer.append(observer)
    def remove_observer(self,observer:Observer):
        self.__observer.remove(observer)
    def notify(self):
        for observer in self.__observer:
            observer.update(self.__temperature)