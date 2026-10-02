from abc import ABC,abstractmethod

class NotificationService(ABC):
    def send(self,to:str,title:str,body:str):
        pass
    

class EmailNotificationService(NotificationService):
    def send(self,to:str,title:str,body:str):
        print("Sending email through email notification service")
        print(f"TO {to}")
        print(f"Title {title}")
        print(f"body {body}")


        

class SendEmailGridService:
    def send_email(self,reciept:str,subject:str,content:str):
        print("Sending email through send email grid service")
        print(f"TO {reciept}")
        print(f"Title {subject}")
        print(f"body {content}") 


class EmailAdapterService(NotificationService):
    def __init__(self,grid_service:SendEmailGridService):
        self.__grid_service=grid_service
        
    def send(self,to:str,title:str,body:str):
        self.__grid_service.send_email(to,title,body)
        
        
class OrderService:
    def __init__(self,email_service:NotificationService):
        self.__email_service=email_service
    
    def create_order(self):
        self.__email_service.send("lakshyavarshney62@gmail.com",'Orderplaced',"order executed take 10min")


grid_service=SendEmailGridService()      
adapter =EmailAdapterService(grid_service)

   
service=OrderService(adapter)
service.create_order()