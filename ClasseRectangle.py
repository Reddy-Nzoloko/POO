# creation de la class
class Rectangle:
    def __init__(self, longeur, largeur, couleur="red"):
        self.longeur = longeur
        self.largeur = largeur
        self.couleur = couleur
        
    def calcule_surface(self):
        return self.longeur * self.largeur   
    
    
# instatiation du rectangle
rectangles = Rectangle(5, 3)
print("Voici notre longeur ", rectangles.longeur)
print("Voici notre largeur ", rectangles.largeur)
print("Voici la couleur de notre rectagle ", rectangles.couleur)
print("La surfance est de ", rectangles.calcule_surface())
