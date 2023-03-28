 #LAB tehtävä 02

rekisterit = []

while True:
    annettu_rekisteri = input("Anna rekisterinumero: ").upper()
    if annettu_rekisteri == "":      
        break
    else: 
        rekisterit = rekisterit + [annettu_rekisteri]

jarjestys = sorted(rekisterit)
kaikki = ", ".join(jarjestys)
print(kaikki)