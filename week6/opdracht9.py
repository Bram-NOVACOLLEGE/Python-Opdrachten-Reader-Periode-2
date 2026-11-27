class Persoon:
    def __init__(self, naam):
        self.naam = naam

    def stel_voor(self):
        print(f"Hoi, ik ben {self.naam}")

Persoon = Persoon("Bram")
Persoon.stel_voor()