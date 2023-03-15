#LAB03 tehtävä 04

#Teksti komennot
print("Anna pistemäärä")
num = int(input("Pisteet: "))

# #printti komennot
if num == 0 or num == 1:
     print("Arvosana: 0")
elif num == 2 or num == 3:
     print("Arvosana: 1")
elif num == 4 or num == 5:
    print("Arvosana: 2")
elif num == 6 or num == 7:
     print("Arvosana: 3")
elif num == 8 or num == 9:
     print("Arvosana: 4")
elif num == 10 or num == 11 or num == 12:
     print("Arvosana: 5")
else:
     print("Annoit väärän pistemäärän, anna uusi pistemäärä!")