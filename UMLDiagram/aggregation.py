from typing import List

class Student:
    def __init__(self,name:str,roll_no:int)->None:
        self.__name=name
        self.__roll_no=roll_no
    def get_name(self)->str:
        return self.__name
    def get_roll_no(self)->int:
        return self.__roll_no
    
class Department:
    def __init__(self,dept:str)->None:
        self.__dept=dept
        self.__students:List[Student]=[]
        
    def add_students(self,student:"Student")->None:
        self.__students.append(student)
    def get_students(self)->None:
        for i in self.__students:
            print(f"{i.get_name()} has roll no. {i.get_roll_no()} and department is  {self.__dept}")
            
if __name__=="__main__":
    student1: Student=Student("Lakshay varshney",23)
    student2: Student=Student("vikalp varshney",25)
    department:Department=Department("computer science")
    department.add_students(student1)
    department.add_students(student2)
    department.get_students()
    