class Laptop:
    processor=None
    ram=None
    graphic_card=None
    color=None
    screen_size=None
    
    def get_laptop(self):
        if self.processor:
            print(f"Processor is {self.processor}")
        if self.ram:
            print(f"Ram is {self.ram}")
        if self.graphic_card:
            print(f"Graphic Card is {self.graphic_card}")
        if self.color:
            print(f"Color is {self.color}")
        if self.screen_size:
            print(f"screen size is {self.screen_size}")

        


class LaptopBuilder:
    def __init__(self):
        self.__laptop=Laptop()
    
    
    def set_processor(self,processor:str):
        self.__laptop.processor=processor
        return self
    
    def set_ram(self,ram:str):
        self.__laptop.ram=ram
        return self
    
    def set_graphic_card(self,graphic_card:str):
        self.__laptop.graphic_card=graphic_card
        return self
    
    def set_color(self,color:str):
        self.__laptop.color=color
        return self
    
    def set_screen_size(self,screen_size:str):
        self.__laptop.screen_size=screen_size
        return self
        
    
    def build(self):
        return self.__laptop
    

l=LaptopBuilder().set_processor('ies-234').set_color('white').build()
l.get_laptop()
##print