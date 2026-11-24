prijs = float(input("Wat is de prijs? "))
lid = input("Ben je lid? (ja/nee): ")

if lid == "ja":
    korting = prijs * 0.10
    nieuwe_prijs = prijs - korting
    print(f"Met 10% korting betaal je {nieuwe_prijs} euro.")
else:
    print(f"Zonder korting betaal je {prijs} euro.")