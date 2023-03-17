#LAB04 tehtävä 05

#Teksti komennot
fname = input("Anna etunimesi: ")
sname = input("Anna sukunimesi: ")
eka = fname[0]
letter = len(fname)

#printti komennot
print(eka * letter, sname[::-1])