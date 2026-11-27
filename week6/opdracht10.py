class Klant:
    def __init__(self, klant_id, naam, telefoonnummer):
        self.klant_id = klant_id
        self.naam = naam
        self.telefoonnummer = telefoonnummer

    def __str__(self):
        return f"Klant {self.klant_id}: {self.naam} (Telefoonnummer: {self.telefoonnummer})"

    def controleer_telefoonnummer(self):
        if len(self.telefoonnummer) != 10:
            print(f"Waarschuwing: Het telefoonnummer van {self.naam} ({self.telefoonnummer}) bestaat niet uit 10 cijfers!")


def maak_klanten():
    klanten = [
        Klant(1, "Bram", "0611182929"),
        Klant(2, "Jan", "069123292"),
        Klant(3, "Paul", "069234983298"),
        Klant(4, "Anna", "068929293"),
        Klant(5, "Henk", "0698298189219"),
    ]
    return klanten


klanten_lijst = maak_klanten()

for klant in klanten_lijst:
    print(klant)
    klant.controleer_telefoonnummer()