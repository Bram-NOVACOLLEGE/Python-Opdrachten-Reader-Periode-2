leeftijd = int(input("Voer je leeftijd in:"))

if leeftijd < 13:
    print("Kind")
elif leeftijd <= 17:
    print("Tiener")
else:
    print("Volwassene")