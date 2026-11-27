try:
    getal = float(input("Voer een getal in:"))
    print(f"Je hebt {getal} ingevoerd")
except ValueError:
    print("Ongeldige invoer")
