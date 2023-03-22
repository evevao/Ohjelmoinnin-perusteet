#LAB05 tehtävä 03

print("Lasketaan alla lukujen keskiarvo.")
print("Anna alla kolme numeroa.")

#Teksti komennot
num1 = float(input("Anna luku yksi: "))
num2 = float(input("Anna luku kaksi: "))
num3 = float(input("Anna luku kolme: "))

#funktio komento
def average():
    return print("Keskiarvo:", str(round(((num1+num2+num3)/3), 2)))
average()