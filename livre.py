class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.__titre = titre
        self.auteur = auteur
        self.genre = genre
        self.prix = prix

    # Méthodes getter
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.auteur

    def get_genre(self):
        return self.genre

    def get_prix(self):
        return self.prix

    # Méthodes setter
    def set_titre(self, titre):
        self.titre = titre

    def set_auteur(self, auteur):
        self.auteur = auteur

    def set_genre(self, genre):
        self.genre = genre

    def set_prix(self, prix):
        self.prix = prix

    def afficher_details(self):
        print("Titre:", self.titre)
        print("Auteur:", self.auteur)
        print("Genre:", self.genre)
        print("Prix:", self.prix)


class Librairie:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.get_titre()] = livre
    def supprimer_livre(self, titre):
        if titre in self.livres:
            del self.livres[titre]
            print(f"Le livre '{titre}' a été supprimé de la librairie.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans la librairie.")

    def chercher_livre(self, titre):
        if titre in self.livres:
            livre = self.livres[titre]
            print("Détails du livre recherché:")
            livre.afficher_details()
        else:
            print(f"Le livre '{titre}' n'a pas été trouvé dans la librairie.")


# Fonction pour saisir les détails d'un livre
def saisir_details_livre():
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez le nom de l'auteur du livre : ")
    genre = input("Entrez le genre du livre : ")
    prix = float(input("Entrez le prix du livre : "))
    return Livre(titre, auteur, genre, prix)


# Fonction pour afficher le menu
def afficher_menu(): 
    try:
        print("\n Votre Menu de Choix! :")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Rechercher un livre")
        print("4. Quitter") 
    except ValueError:
       print("impossible de faire cette operation")

# Test de code
librairie = Librairie()

# Boucle pour afficher le menu et demander à l'utilisateur d'effectuer une action
while True:
    afficher_menu()
    choix = input("Entrez le numéro de l'option que vous souhaitez sélectionner : ")

    if choix == "1":
        livre = saisir_details_livre()
        librairie.ajouter_livre(livre)
    elif choix == "2":
        titre_supprimer = input("Entrez le titre du livre que vous souhaitez supprimer : ")
        librairie.supprimer_livre(titre_supprimer)
    elif choix == "3":
        titre_recherche = input("Entrez le titre du livre que vous souhaitez rechercher : ")
        librairie.chercher_livre(titre_recherche)
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez entrer un numéro valide.")
