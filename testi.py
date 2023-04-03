

tiedoston_nimi = "LAB09_02_nimet.txt"
tiedosto = open(tiedoston_nimi, "w+")
nimi = "*"
rivi = 0

print("Anna alla henkilön sukunimi tai jatka eteenpäin Enter-painikkeella.")

while nimi != "":
    nimi = input("Anna sukunimi: ")
    if nimi != "":
        tiedosto.write(nimi + "\n")
        rivi += 1
print(rivi, "Nimeä kirjoitettu tiedostoon.")

dump = input("Paina Enter-painiketta näkeäksesi kirjoitetut nimet.")
teidosto = open(tiedoston_nimi, "r")
lines = tiedosto.readlines()
print(lines)
tiedosto.close()
print(lines)