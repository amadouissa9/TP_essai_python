"""Écrivez une fonction appelée factorielle qui prend un entier en entrée et
renvoie sa factorielle.
"""
def factorielle(nbr):
    if nbr < 0:
         return None
    elif nbr == 0:
        return 1 
    else:
        resultat = 1
        for i in range(1, nbr + 1):
            resultat *= i
        return resultat
while True :
      try :
        nombre = int(input("Entrez le nombre a factoriser : "))
        break
      except ValueError :
        print("veuillez entrez un nombre positif ")
resultat = factorielle(nombre)
if resultat is not None:
    print("La factorielle de", nombre, "est :", resultat)
else:
    print("Veuillez entrer un entier positif.")
