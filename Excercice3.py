nom = "Reddy"
Age = 22
Taille = 65.5
Etudiant = True
print(f"Mon nom est {nom} j'ai {Age} ans je mesure {Taille} je suis Etudiants, {Etudiant}...")   
print(type(nom), type(Age), type(Taille), type(Etudiant))

# liste
ReseauxSociaux = ["Facebook", "Intagrame", "TikTok"]
# Ajout d'un element dans la liste
ReseauxSociaux.append("Threds")
print(ReseauxSociaux)
ReseauxSociaux.remove("Facebook")
print(ReseauxSociaux)
print(len(ReseauxSociaux))

Nombre = [1, 2, 3, 4, 5, 6]
10 in Nombre
Nombre.sort()
Sociale = ["Jeans", "Amele", "Mangese", "Xavier"]
print(Sociale)
Sociale.sort()
print(Sociale)

# Creation du dictionnaire

NouvelleCampagne = {
    "Rensponsable_de_campagne": "Jeanne d'arc",
    "Nom_de_campagne": "Nous aimons les cheins",
    "date_de_debut": "01/01/2025",
    "Infuenceur_Important": ["Mont_chien", "@MeilleursFriandeur pour chien"]
}
print(NouvelleCampagne["Infuenceur_Important"])
# Ajout d'un element dans le dictionnaire
NouvelleCampagne["Nom scientifique"] = "Jamal"
print(NouvelleCampagne["Nom scientifique"])
