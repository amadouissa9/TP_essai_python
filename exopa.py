def pair(nombre) :
    if (nombre % 2 == 0):
     return True
    else :
        return False
    
while True :
    try :
        nbr = int (input("entres le monbre : "))
        break
    except ValueError :
        print("impossble")
resultat = pair(nbr)
print("le resultat est",resultat)
