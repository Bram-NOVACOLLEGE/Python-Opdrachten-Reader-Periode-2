try:
    getal = float(input("Voer een getal in:"))
    print(f"Je hebt {getal} ingevoerd")
except ValueError:
    print("Ongeldige invoer")

# Bij een lege invoer geeft hij Ongeldige invoer.
# Bij tekst geeft die ook Ongeldige invoer.