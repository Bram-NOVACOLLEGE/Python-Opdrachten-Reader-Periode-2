class Persoon:
    def __init__(self, naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def toon_info(self):
        print(f"Mijn naam is {self.naam} en ik ben {self.leeftijd} jaar oud")

Persoon = Persoon("Bram", 17)
Persoon.toon_info()