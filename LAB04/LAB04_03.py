#LAB04 tehtävä 03

#Teksti komennot
sum = 0
rivi = 0
teksti = "Lukuja annettu: "
teksti2 = "Lukujen summa: "


#printti komennot
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    else: 
        luku2 = int(luku)
        sum += luku2
        rivi += 1

print(teksti,rivi)
print(teksti2,sum)