#LAB09 tehtävä 01


tiedoston_nimi = "LAB09_01_nimet.txt"
tiedosto = open(tiedoston_nimi, "w")
nimi = "*"
i = 0

print("Anna alla henkilön sukunimi tai jatka eteenpäin Enter-painikkeella.")

while nimi != "":
    nimi = input("Anna sukunimi: ")
    if nimi != "":
        tiedosto.write(nimi + "\n")
        i += 1
tiedosto.close()
print(i, "Nimeä kirjoitettu tiedostoon.")