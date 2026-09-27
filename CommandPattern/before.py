class Chef:
    def cook_pasta(self):
        print("chef is cooking pasta")
        
    def cook_pizza(self):
        print("chef is cooking pizza")
    
    def cook_burger(self):
        print("chef is cooking burger")

class Waiter:
    def __init__(self,chef:Chef):
        self.__chef=chef
    
    def take_order(self,order):
        if order=="pizza":
            self.__chef.cook_pizza()
        if order=="pasta":
            self.__chef.cook_pasta()
        if order=="burger":
            self.__chef.cook_burger()
        if order  not in  ("pizza", "burger","pasta"):
            print("this is not present")


chef=Chef()
waiter=Waiter(chef)

waiter.take_order("pizza")
waiter.take_order("colddrink")