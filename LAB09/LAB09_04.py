#LAB09 tehtävä 04

nimilista = {}
lukumäärä = 0

with open("nimet.txt", "r") as tiedosto:
    for nimi in tiedosto:
        nimilista[lukumäärä] = nimi
        value = nimi.split()
        lukumäärä = lukumäärä + 1

print("Nimiä listassa on:", lukumäärä)

kuinkaMonta = {value: list(nimilista.values()).count(value) for value in nimilista.values()}
print(kuinkaMonta)