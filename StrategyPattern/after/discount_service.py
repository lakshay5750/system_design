from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self,discount_strategy:DiscountStrategy):
        self.__discount_strategy=discount_strategy
    
    def set_strategy(self,strategy:DiscountStrategy):
        self.__discount_strategy=strategy
    
    def process(self):
        self.__discount_strategy.discount()
        