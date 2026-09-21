class User:
    def __init__(self,name:str,email_address:str,age:int)->None:
        self.__name=name
        self.__email_address=email_address
        self.__age=age
    
    def get_user_info(self):
        return f"{self.__name} is currently visiting website of age {self.__age}"
    def get_user_name(self)->str:
        return self.__name
    
    def is_adult(self)->bool:
        return self.__age>18