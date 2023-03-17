#LAB04 tehtävä 03

#Teksti komennot
sum = 0
letter = 0
annettu = "Lukuja annettu: "


#printti komennot
while True:
    luku = int(input("Anna luku: "))
    letter += 1 
    if luku == 0:
        print(annettu, letter)
        break
    else:
        sum = sum + luku

print("Lukujen summa: ", sum)

#Toimii vain numeorilla. Ei hyväksy input(" ")