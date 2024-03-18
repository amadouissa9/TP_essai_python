"""
Écrivez une fonction appelée tri_croissant qui prend une liste de nombres
en entrée et renvoie une nouvelle liste contenant les mêmes éléments triés
par ordre croissant.
"""
def creer_liste ():
    liste = []
    # control de saisir pour la taille de la liste 
    """while True:
        try:
            taille = int(input("saisir la taille de votre liste :"))
            if taille =='q':
                break
            if taille > 0 :
                break
            else :
                print("saisit un nombre positif SVP !")
        except ValueError:
            print ("vellez entres un monbre SVP !")
            """
    # remplissage de la liste 
    """ while True :
       # try :
            for i in range (1,taille):
                element = int(input(f"entrez votre {i} element :"))
                break
                element.append
    """
    while True:
        try:
            while True:
                element = input(f"Entrez votre {len(liste)+1}ème élément (ou q pour arreter) : ")
                if element.lower() == 'q':
                    break
                liste.append(int(element))
            break
        except ValueError:
            print("On a besoin que des nombres")

    return liste

def tri_croissant(liste:list):
    return sorted(liste)


liste = creer_liste()
liste_trie = tri_croissant(liste)
print(liste_trie)  




