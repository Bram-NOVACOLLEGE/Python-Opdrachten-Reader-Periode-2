try:
    getal1 = float(input("Voer het eerste getal in: "))
    getal2 = float(input("Voer het tweede getal in: "))

    uitkomst = getal1 / getal2
    print(f"De uitkomst van {getal1} gedeeld door {getal2} is: {uitkomst}")

except ZeroDivisionError:
    print("Je kunt niet delen door nul")