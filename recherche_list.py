class ListePersonnes:
    def __init__(self):
        self.liste_personnes = []

    def ajouter_personne(self, nom, age):
        if isinstance(age, int) and age > 0:  # Vérification de l'âge valide
            self.liste_personnes.append(self.Personne(nom, age))
            print("Personne ajoutée avec succès.")
        else:
            print("L'âge doit être un entier positif.")

    def afficher_personnes(self):
        if self.liste_personnes:
            for personne in self.liste_personnes:
                print(personne)
        else:
            print("La liste est vide.")

    def rechercher_personne(self, nom):
        personnes_trouvees = [personne for personne in self.liste_personnes if personne.nom == nom]
        if personnes_trouvees:
            print("Personnes trouvées :")
            for personne in personnes_trouvees:
                print(personne)
        else:
            print(f"Aucune personne nommée '{nom}' trouvée dans la liste.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        personnes_filtrees = [personne for personne in self.liste_personnes if min_age <= personne.age <= max_age]
        if personnes_filtrees:
            print("Personnes dont l'âge est compris entre", min_age, "et", max_age, ":")
            for personne in personnes_filtrees:
                print(personne)
        else:
            print(f"Aucune personne dont l'âge est compris entre {min_age} et {max_age} n'a été trouvée.")

