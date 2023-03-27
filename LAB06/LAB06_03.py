#LAB06 tehtävä 03

#Teksti komennot
rivi = 0
teksti = "Oppilaita: "
teksti2 = "Lukujen summa: "
my_list = []
tulos = ""


#printti komennot

   
while True:
    user_input = input("Anna oppilaan nimi: ")
    if user_input == "":      
        break
    else: 
        rivi += 1
        my_list = my_list + [user_input]

print(teksti, rivi)

i = 0
while i < len(my_list):
    if i == len(my_list) - 1:
        tulos = tulos + my_list[i]
    else:
        tulos = tulos + my_list[i] + ", "
    i = i + 1
    
print(tulos)