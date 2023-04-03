#LAB09 tehtävä 02


with open("LAB09_01_nimet.txt", "r") as tiedosto:
    sisalto = tiedosto.read().splitlines()

jarjestyksessa = sorted(sisalto)

print(jarjestyksessa)
tiedosto.close()