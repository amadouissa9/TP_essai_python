from reservation import SalleCinema

def main():
    # Création de la salle de cinéma
    salle = SalleCinema(capacite=50, places_speciales=5)

    # Exemples d'utilisation des méthodes de la classe SalleCinema
    salle.reserver_place("Alice", 10)
    salle.reserver_place("Bob", 25)
    salle.reserver_place("Charlie", 7)
    salle.reserver_place_speciale("David")
    salle.afficher_places_reserves()
    salle.nombre_places_disponibles()
    salle.filtrer_reservations_par_personne("Alice")
    salle.annuler_reservation("Bob")
    salle.nombre_places_disponibles()

if __name__ == "__main__":
    main()
