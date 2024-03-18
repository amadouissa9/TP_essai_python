class SalleCinema:
    def __init__(self, capacite, places_speciales):
        self.capacite = capacite
        self.places_disponibles = capacite
        self.places_reserves = {}
        self.places_speciales = places_speciales
        self.places_speciales_reserves = {}

    def reserver_place(self, nom, place):
        if place in self.places_reserves or place in self.places_speciales_reserves:
            print(f"La place {place} est déjà réservée.")
        elif place <= self.capacite:
            if nom in self.places_reserves.values() or nom in self.places_speciales_reserves.values():
                print(f"{nom} a déjà réservé une place.")
            else:
                if place <= self.capacite - len(self.places_reserves) - len(self.places_speciales_reserves):
                    if place > self.capacite - len(self.places_reserves):
                        self.places_speciales_reserves[place] = nom
                    else:
                        self.places_reserves[place] = nom
                    self.places_disponibles -= 1
                    print(f"{nom} a réservé la place {place}.")
                else:
                    print("Désolé, plus de places disponibles.")
        else:
            print("Numéro de place invalide.")

    def afficher_places_reserves(self):
        print("Places réservées :")
        for place, nom in self.places_reserves.items():
            print(f"Place {place}: {nom}")
        print("Places spéciales réservées :")
        for place, nom in self.places_speciales_reserves.items():
            print(f"Place spéciale {place}: {nom}")

    def nombre_places_disponibles(self):
        print(f"Il reste {self.places_disponibles} places disponibles.")

    def filtrer_reservations_par_personne(self, nom):
        reservations = {place: nom for place, n in self.places_reserves.items() if n == nom}
        reservations.update({place: nom for place, n in self.places_speciales_reserves.items() if n == nom})
        if reservations:
            print(f"Réservations pour {nom} :")
            for place, nom in reservations.items():
                print(f"Place {place}")
        else:
            print(f"Aucune réservation pour {nom}.")

    def annuler_reservation(self, nom):
        removed = []
        for place, n in list(self.places_reserves.items()):
            if n == nom:
                removed.append(place)
                del self.places_reserves[place]
                self.places_disponibles += 1
        for place, n in list(self.places_speciales_reserves.items()):
            if n == nom:
                removed.append(place)
                del self.places_speciales_reserves[place]
                self.places_disponibles += 1
        if removed:
            print(f"Les réservations pour {nom} ont été annulées pour les places suivantes : {removed}.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    def reserver_place_speciale(self, nom):
        for place in range(1, self.places_speciales + 1):
            if place not in self.places_reserves and place not in self.places_speciales_reserves:
                self.places_speciales_reserves[place] = nom
                self.places_disponibles -= 1
                print(f"{nom} a réservé une place spéciale (place {place}).")
                return
        print("Désolé, plus de places spéciales disponibles.")
