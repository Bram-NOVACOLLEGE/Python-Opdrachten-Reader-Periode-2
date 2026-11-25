gewicht = float(input("Wat is je gewicht in kg?"))
lengte = float(input("Wat is je lengte in meters?"))

bmi = gewicht / (lengte ** 2)
bmi = round(bmi, 1)

print(f"Je BMI is {bmi}")

if bmi < 18.5:
    print("Categorie: ondergewicht")
elif bmi < 25:
    print("Categorie: gezond gewicht")
else:
    print("Categorie: overgewicht")