class Etudiant:
    #Creation d'un constructeur permettant l'instanciation de la classe.
    #Constructeur est une fonction.
    #self désigne l'objet courant.
    etudiant_cree = 0 # Variable de classe. Une variable indépendante de tout objet de cette classe.
    def __init__(self, nom, prenom, age, niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.niveau = niveau
        Etudiant.etudiant_cree += 1
        print(f"Creation de l' étudiant {Etudiant.etudiant_cree}")
    def infos(self):
        print("----------------------------------------------------------------------")
        print(f"Nom: {self.nom},\n Prenom: {self.prenom},\n age: {self.age} ans,\n niveau d'étude: {self.niveau}\n")
        print("----------------------------------------------------------------------")


# Création d'un objet : création d'un étudiant.
#print("----------------------------------------------------------------------")
e1 = Etudiant("Labrie", "Stéphane", 38, "AEC")
e1.infos()

e2 = Etudiant("Diallo", "Abdou", 28, "Maitrise")
e2.infos()

e3 = Etudiant("Eyong", "Bijou", 22, "Bac")
e3.infos()

e4 = Etudiant("St-Pierre", "Maxime", 16, "Doctorat")
e4.infos()