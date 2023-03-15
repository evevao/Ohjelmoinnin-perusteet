#LAB02 tehtävä 03

#Teksti komennot
nimi = input("Anna nimesi: ")
Etunimi, *Sukunimi = nimi.split()

#printti komennot?
print("Etunimi: {Etunimi}".format (Etunimi=Etunimi))
print("Sukunimi: {Sukunimi}".format (Sukunimi=" ".join (Sukunimi)))