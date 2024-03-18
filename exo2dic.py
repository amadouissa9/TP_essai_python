# Création du dictionnaire personne avec les informations
personne = {
    "nom": "Amadou",
    "âge": 30,
    "ville": "Niamey"
}

# Affichage de la valeur associée à la clé "âge"
print("Âge de la personne :", personne["âge"])

# Modification de la valeur associée à la clé "ville" pour "Paris"
personne["ville"] = "Niger"

# Ajout d'une nouvelle paire clé-valeur pour représenter le sexe de la personne
personne["sexe"] = "masculin"

# Suppression de la clé "ville" du dictionnaire
del personne["ville"]

# Affichage du dictionnaire résultant
print("Dictionnaire résultant :", personne)
