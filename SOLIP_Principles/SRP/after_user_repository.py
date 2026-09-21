from after_user import User



class UserRepository:
    def __init__(self,db,name,password)->None:
        self.__db=db
        self.__name=name
        self.__password=password
    
    def save_to_database(self,user:"User"):
         return f"{user.get_user_name()} is saved to database"
            
    def delete_from_database(self,user:"User"):
                return f"{user.get_user_name()} is deleted from the database"
        