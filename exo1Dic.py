# Création de la liste contenant les entiers de 1 à 5
nombres = [1, 2, 3, 4, 5]

# Ajout des entiers de 6 à 10 à la fin de la liste
nombres.extend([6, 7, 8, 9, 10])

# Affichage de la longueur de la liste
print("Longueur de la liste :", len(nombres))

# Suppression du nombre 3 de la liste
nombres.remove(3)

# Tri de la liste dans l'ordre décroissant
nombres.sort(reverse=True)

# Affichage de la liste résultante
print("Liste résultante :", nombres)
