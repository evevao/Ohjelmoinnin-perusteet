#LAB02 tehtävä 04

import datetime

#Teksti komennot
fname = input("Anna etunimesi: ")
ika = int((input("Syntymävuotesi: ")))
ika2 = datetime.datetime.today()
ika3 = int(ika2.year)
ika4 = (ika3 - ika)

#Printti komennot
print("Hei", fname, ", olet", ika4 , "vuotta.")