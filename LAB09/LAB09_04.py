#LAB09 tehtävä 04

nimilista = {}
key = 0

with open("nimet.txt", "r") as tiedosto:
    for nimi in tiedosto:
        nimilista[key] = nimi
        value = nimi.split()
        key = key + 1

print("Nimiä listassa on:", key)

kuinkaMonta = {value: list(nimilista.values()).count(value) for value in nimilista.values()}
print(kuinkaMonta)