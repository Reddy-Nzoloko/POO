class Animal:
    def crier(self):
        print("un cris d'animal")
        
        
class Chien(Animal):
    def crier(self):
        print("wouh waouh")
        

class Chat(Animal):
    def crier(self):
        print("miaouh")
        
        
class Inconnue(Animal):
    def crier(self):
        return super().crier()
    
    
animal = Animal()
cri_animal = animal.crier()

chien = Chien()
cri_chien = chien.crier()

chat = Chat()
cris_chat = chat.crier()

inconnueAn = Inconnue()
crisInconnue = inconnueAn.crier()     
        
