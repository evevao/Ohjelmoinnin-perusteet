#LAB09 tehtvä 03

tiedoston_nimi = "LAB09_03_luvut.txt"
tiedosto = open(tiedoston_nimi, "w")
luku = "*"
rivi = 0

print("Anna alla luku tai jatka eteenpäin Enter-painikkeella.")

while luku != "":
    luku = input("Anna luku: ")
    if luku != "":
        tiedosto.write(luku + "\n")
        rivi += 1
tiedosto.close()
print("Syötetty", rivi, "lukua.")