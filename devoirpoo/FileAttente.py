class FileAttente:
    def __init__(self):
        self.file_attente = []
        self.file_prioritaire = []

    def ajouter_personne_en_attente(self, nom):
        self.file_attente.append(nom)
        print(f"{nom} a été ajouté à la file d'attente.")

    def ajouter_personne_prioritaire(self, nom):
        self.file_prioritaire.append(nom)
        print(f"{nom} a été ajouté en tant que personne prioritaire.")

    def supprimer_personne_de_attente(self):
        if self.file_prioritaire:
            personne_supprimee = self.file_prioritaire.pop(0)
            print(f"{personne_supprimee} a été supprimé de la file d'attente prioritaire.")
        elif self.file_attente:
            personne_supprimee = self.file_attente.pop(0)
            print(f"{personne_supprimee} a été supprimé de la file d'attente.")
        else:
            print("La file d'attente est vide.")
