#LAB04 tehtävä 04

#Tekstikomennot
luku = int(input("Anna numero väliltä 1-10: "))
rivi = int(1)

#printti komennot
for i in range(1, int(luku) + 1):
    print("luvun",rivi, "neliö on", i ** 2)
    rivi = rivi + int(1)