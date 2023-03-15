#LAB04 tehtävä 01

#Teksti komennot
luku = int(input("Montako lukua: "))
rivi = int(1)

#printti komennot
for i in range(int(luku)):
    print(rivi, "luku on: ", i * 10)
    rivi = rivi + int(1)