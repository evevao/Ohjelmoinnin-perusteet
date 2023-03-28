#LAB08 tehtävä 03

arvosanat = []
rivi = 0
print("Anna arvosanoja 0-5")


while True:
    annnetut_arvosanat = input("Anna arvosana: ")
    if annnetut_arvosanat == "":
        break
    else:
        rivi += 1
        arvosanat = arvosanat + [float(annnetut_arvosanat)]

summa = sum(arvosanat)
keskiarvo = str(round(summa / rivi, 2))

print("Arvosanoja yhteensä:", rivi)
print("Arvosanojen keskiarvo:", keskiarvo)