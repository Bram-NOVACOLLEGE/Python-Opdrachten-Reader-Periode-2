getal1 = float(input("Voer een getal in:"))
getal2 = float(input("Voer nog een getal in:"))

if getal1 > getal2:
    print(f"{getal1} is het grootst.")
elif getal2 > getal1:
    print(f"{getal2} is het grootst.")
else:
    print("De getallen zijn gelijk.")