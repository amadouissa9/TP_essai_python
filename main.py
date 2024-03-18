from reservation import SalleCinema

def afficher_menu():
    print("\nMenu principal :")
    print("1. Réserver une place")
    print("2. Afficher les places réservées")
    print("3. Afficher le nombre de places disponibles")
    print("4. Filtrer les réservations par personne")
    print("5. Annuler une réservation")
    print("6. Réserver une place spéciale")
    print("7. Quitter")

def main():
    salle = SalleCinema(capacite=50, places_speciales=5)

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            nom = input("Entrez votre nom : ")
            place = int(input("Entrez le numéro de la place : "))
            salle.reserver_place(nom, place)
        elif choix == "2":
            salle.afficher_places_reserves()
        elif choix == "3":
            salle.nombre_places_disponibles()
        elif choix == "4":
            nom = input("Entrez le nom de la personne : ")
            salle.filtrer_reservations_par_personne(nom)
        elif choix == "5":
            nom = input("Entrez le nom de la personne dont vous souhaitez annuler la réservation : ")
            salle.annuler_reservation(nom)
        elif choix == "6":
            nom = input("Entrez votre nom : ")
            salle.reserver_place_speciale(nom)
        elif choix == "7":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

if __name__ == "__main__":
    main()

