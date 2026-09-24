class DiscountService:
    def calculate_discount(self,discount_way):
        if discount_way=="Diwali":
            print("Diwali discounted price is 15%")
        if discount_way.lower()=="college_student":
            print("Student give discount flat 20% off on accessories")
            
            
            

discount=DiscountService()
discount.calculate_discount("College_student")