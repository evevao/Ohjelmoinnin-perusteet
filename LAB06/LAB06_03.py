#LAB06 tehtävä 03

#Teksti komennot
rivi = 0
teksti = "Oppilaita: "
teksti2 = "Lukujen summa: "
oppilaat = []
tulos = ""


#printti komennot

   
while True:
    annetut = input("Anna oppilaan nimi: ")
    if annetut == "":      
        break
    else: 
        rivi += 1
        oppilaat = oppilaat + [annetut]

print(teksti, rivi)

i = 0
while i < len(oppilaat):
    if i == len(oppilaat) - 1:
        tulos = tulos + oppilaat[i]
    else:
        tulos = tulos + oppilaat[i] + ", "
    i = i + 1
    
print(tulos)