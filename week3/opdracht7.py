leeftijd = int(input("Wat is je leeftijd? "))
id = input("Heb je een geldig ID? (ja/nee): ")

if leeftijd >= 18 and id == "ja":
    print("Je mag het product kopen.")
else:
    print("Je mag het product niet kopen.")