def moyenne(liste):
    if len(liste) == 0:
        return None 
    else:
        return sum(liste) / len(liste)


liste_nombres = []

while True:
    try : 
        tail = int(input("entres la taille de la liste : "))
        break
    except ValueError :
        print("impossble")
    entree == input("Entrez un nombre : ")
    if entree.lower() == 'fin'
        break
    try:
        nombre = float(entree)
        liste_nombres.append(nombre)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

resultat = moyenne(liste_nombres)
if resultat is not None:
    print("La moyenne des nombres dans la liste est :", resultat)
else:
    print("La liste est vide.")


