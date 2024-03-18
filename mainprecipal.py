
import recherche_list as rl
from devoirpoo import FileAttente as F

def main():
    liste = rl.ListePersonnes()
    file_attente = F.FileAttente()
    
    while True:
        print("\nMenu principal :")
        print("1. Ajouter une personne")
        print("2. Afficher les personnes")
        print("3. Rechercher une personne par nom")
        print("4. Filtrer les personnes par âge")
        print("5. Gérer la file d'attente")
        print("6. Quitter")
        
        choix = input("Entrez votre choix : ")

        if choix == "1":
            nom = input("Entrez le nom de la personne : ")
            while True:
                age_input = input("Entrez l'âge de la personne : ")
                try:
                    age = int(age_input)
                    if age < 0:
                        print("Veuillez entrer un âge positif SVP !")
                    else:
                        liste.ajouter_personne(nom, age)
                        break
                except ValueError:
                    print("Veuillez entrer un âge valide (entier).")
        elif choix == "2":
            print("\nPersonnes dans la liste :")
            liste.afficher_personnes()
        elif choix == "3":
            nom = input("Entrez le nom de la personne à rechercher : ")
            liste.rechercher_personne(nom)
        elif choix == "4":
            min_age = int(input("Entrez l'âge minimum : "))
            max_age = int(input("Entrez l'âge maximum : "))
            liste.filtrer_personnes_par_age(min_age, max_age)
        elif choix == "5":
            F.gestion_file_attente(file_attente)
        elif choix == "6":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()

