from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self):
        pass
    
    def work(self):
        pass
    def eat(self):
        pass


class Human(Employee):
    def __init__(self):
        super().__init__()
        pass
    
    def work(self):
        print("hUman is working")
        
    def eat(self):
        print("hUman is eating")
        
class Robot(Employee):
    def __init__(self):
        super().__init__()
        pass
        
    def work(self):
        print("hUman is working")
            
    def eat(self):
        print(Exception("eating of robot not possible"))
        
human=Human()
human.eat()
human.work()
robot=Robot()
robot.work()
robot.eat()
    