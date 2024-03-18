# Création de la liste de dictionnaires représentant des étudiants
etudiants = [
    {"nom": "Nasser", "note": 15},
    {"nom": "Karim", "note": 8},
    {"nom": "Boubacar", "note": 12},
    {"nom": "David", "note": 10},
    {"nom": "Eva", "note": 18}
]

# Affichage des noms des étudiants ayant obtenu une note supérieure ou égale à 10
print("Noms des étudiants ayant obtenu une note supérieure ou égale à 10 :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])
