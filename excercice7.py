# Fonction pour calculer le salaire mensuel
def salaire_mensuel(salairesAnnuel):
    Salaire = salairesAnnuel / 12
    return Salaire


# Fonction pour calculer le salaire Hebdomadaire
def salaire_hebdomadaire(salairesMensuel):
    Salaire = salairesMensuel / 4
    return Salaire

# Fonction pour calculer le salaire horaire 


def salaire_horaire(salaireHebdomadaire, nmbreHeureTravailler):
    salaire = salaireHebdomadaire / nmbreHeureTravailler
    return salaire


# appel de la fonction pour le salaire annuel 
inpSAnnuel = int(input("Taper votre salaire "))
salaireM = salaire_mensuel(inpSAnnuel)
print(f"Votre salaire mensuel est de {salaireM} $")

# appel de la fonction pour le salaire mensuel 
sMensue = int(input("Taper votre salaire mensuel "))
salaireHebdo = salaire_hebdomadaire(sMensue)
print(f" Votre salaire Hebdomadaire est de  {salaireHebdo} $") 

# appel de la focntion pour le salaire horaire
sHebdo = int(input("taper votre salaire hebdomadaire "))
sNombre = int(input("Nombre d'heure travailler "))
salaireH = salaire_horaire(sHebdo, sNombre)
print(f"Votre salaire horaire est de {salaireH} $")



