class Persoon:
    def __init__(self, naam, leeftijd, woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats

    def toon_info(self):
        print(f"Hoi, mijn naam is {self.naam}")
        print(f"Hoi, mijn leeftijd is {self.leeftijd}")
        print(f"Hoi, mijn woonplaats is {self.woonplaats}")

Persoon = Persoon("Bram", 17, "Beverwijk")
Persoon.toon_info()