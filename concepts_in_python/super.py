class Phone:
    
    def __init__ (self, price, brand,camera):
        print("inside the phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("buying a redmi phone")

class Smartphone(Phone):
    
    def buy(self):
        print("buying a apple phone")
        super().buy()

s= Smartphone(150000,"apple",128)

s.buy()         
        
    
    