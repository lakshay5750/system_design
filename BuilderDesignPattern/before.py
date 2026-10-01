class Laptop:
    def __init__(
        self,
        processor:str,
        ram:str,
        graphic_card:str=None,
        color:str=None,
        screen_size:str=None
        ):
        self.__processor=processor
        self.__ram=ram
        self.__graphic_card=graphic_card
        self.__color=color
        self.__screen_size=screen_size
    
    def get_laptop(self):
        print(f"Processor is {self.__processor}")
        print(f"Ram is {self.__ram}")
        if self.__graphic_card:
            print(f"Graphic Card is {self.__graphic_card}")
        if self.__color:
            print(f"Color is {self.__color}")
        if self.__screen_size:
            print(f"screen size is {self.__screen_size}")


laptop=Laptop("i5-dghd",16,"iex-1","grey",22)
laptop.get_laptop()
        