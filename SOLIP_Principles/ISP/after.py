from abc import ABC, abstractmethod

class Workable(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def work(self):
        pass
class Eatable(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    
class Human(Workable,Eatable):
    
    def work(self):
        print("workable")
    def eat(self):
        print("eatable")
        
class Robot(Workable):
    def work(self):
        print("workable")


robot=Robot()
robot.work()