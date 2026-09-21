class Student:
    def __init__(self,name:str)->None:
        self.__name=name
        
    def get_name(self)->str:
        return self.__name


class Teacher:
    def __init__(self,name:str)->None:
        self.__name=name
        
    def get_name(self)->str:
        return self.__name
    
    def teach(self,student:"Student")->str:
        return f"{self.__name} is teaching {student.get_name()}"       
    

if __name__=="__main__":
    teacher=Teacher("jatin varshney")
    student=Student("lakshay varshney")
    print(teacher.teach(student))
    