try:
    getal = int(input("Voer een getal in:"))
    print(f"Je hebt het getal {getal} ingevoerd.")
except ValueError:
    print("Dat is geen geldig getal.")