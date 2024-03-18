# Création des listes de noms et d'âges
noms = ["Amadou", "Issa", "Moussa"]
ages = [25, 30, 35]

# Création du dictionnaire personnes en associant chaque nom à son âge
personnes = dict(zip(noms, ages))

# Affichage du dictionnaire personnes
print("Dictionnaire personnes avant l'ajout :", personnes)

# Saisie utilisateur pour le nom et l'âge de la nouvelle personne
nouveau_nom = input("Entrez le nom de la nouvelle personne : ")
nouvel_age = int(input("Entrez l'âge de la nouvelle personne : "))

# Ajout de la nouvelle personne au dictionnaire
personnes[nouveau_nom] = nouvel_age

# Affichage du dictionnaire personnes après l'ajout
print("Dictionnaire personnes après l'ajout :", personnes)
