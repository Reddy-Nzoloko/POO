class Drink:

    def __init__(self, price):
        self.price = price
    
    def drink(self):
        print("je ne sais pas ce que mais je le bois")
        

class Coffe(Drink):
    prices = {"simple": 1, "Serrer": 1, "allonge": 1.5}
    
    def __init__(self, type):
        self.type = type
        super().__init__(price=self.prices.get(type, 1))
    
    def drink(self):
        print(f"un bon café  {self.type} qui coute {self.price}$ pour me reveiller!")
     
        
cafe = Coffe("allonge")
boire = cafe.drink()
               
