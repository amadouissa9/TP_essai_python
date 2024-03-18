"""" Écrivez une fonction appelée tri_croissant qui prend une liste de nombres
en entrée et renvoie une nouvelle liste contenant les mêmes éléments triés
par ordre croissant.
"""
def tri_croissant(la_liste):
    return sorted(la_liste)

def saisir_liste():
    liste = []
    while True:
        element = input("Entrez un élément (ou 'fin' pour terminer) : ")
        if element.lower() == 'fin':
            break
        liste.append(element)
    return liste

while True:
    try:
        taille = int(input("Entrez la taille de votre liste SVP : "))
        if taille < 0:
            print("Veuillez entrer un nombre positif SVP !")
        elif taille == 0:
            print("Impossible d'avoir une liste de 0 élément.")
        else:
            la_liste = []  # Créez une nouvelle liste à chaque itération de la boucle
            for i in range(1, taille + 1):
                try:
                    element = int(input(f"Saisissez le {i}ème élément de la liste : "))
                    la_liste.append(element)
                except ValueError:
                    print("Veuillez entrer un entier valide.")
            break  # Sort de la boucle une fois que la liste est saisie
    except ValueError:
        print("Impossible d'interpréter l'entrée comme un entier.")

# Tri de la liste saisie
nouvelle_liste = tri_croissant(la_liste)
print("La liste triée est :", nouvelle_liste)
