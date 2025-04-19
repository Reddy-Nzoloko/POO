# Creation des dictionnaires
Fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Ajout d'une clé kiwi et de la valeur "vert" dans le dictionnaire
Fruits["kiwi"] = "Vert"
print(Fruits)
# stockage de la valeur de banane dans la variable 
couleurBanane = Fruits["banane"]
print(f"La couleur de la banane est {couleurBanane}")

# Modification de la valeur de la clé Pomme
Fruits["pomme"] = "Vert"
print(f"vooici les fruits et leurs couleurs{Fruits}")

# Suppression d'une clé dans le dictionnaire
del Fruits["banane"]
print(f"ce fruit est bien supprimer voici un aperçu des restants {Fruits}")