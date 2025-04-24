from abc import ABC  # permet de definir des classes de base


class Shape(ABC):
    def area(self):
        return 0
    

# classe     
class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        return self.length * self.length
    

# classe triangle  
class Triangle(Shape):
    def __init__(self, hauteur, base):
        self.hauteur = hauteur
        self.base = base
        
    def area(self):
        return (self.hauteur * self.base)/2


surface = Triangle(hauteur=5, base=7)
surface_triangle = surface.area()
print(f"{surface_triangle} Voilà la surface du premier triangle")

surface1 = Triangle(hauteur=10, base=15)
surface1Triange = surface1.area()
print(f"{surface1Triange} Voilà la surface du deuxième triangle")

'''square = Square(lenght=4)
square_area = square.area()
print(square_area)'''
        