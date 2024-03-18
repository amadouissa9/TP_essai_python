"""
Écrire une fonction appelée est_premier qui prend un entier en entrée et
renvoie True s'il est premier, sinon renvoie False.
"""
def est_premier(nbr):
    if nbr <= 1:
        return False  # Les nombres inférieurs ou égaux à 1 ne sont pas premiers
    elif nbr <= 3:
        return True  # 2 et 3 sont premiers
    elif nbr % 2 == 0 or nbr % 3 == 0:
        return False  # Les multiples de 2 et de 3 ne sont pas premiers
    i = 5
    while i * i <= nbr:
        if nbr % i == 0 or nbr % (i + 2) == 0:
            return False
        i += 6
    return True
while True :
    try :
     nombre = int(input("Entrez un nombre : "))
     break
    except ValueError :
        print("entrez un nombre please !")
if est_premier(nombre):
    print(nombre, "est un nombre premier.")
else:
    print(nombre, "n'est pas un nombre premier.")
