#LAB08 tehtävä 01

kaverit = 10
nimet = []
kaikki = ""


for i in range(kaverit):
    nimi = input("Anna kaverisi nimi: ")
    nimet = nimet + [nimi]
    kaikki = ", ".join(nimet)

nimi = input("Anna kaverisi nimi: ")
nimet = nimet + [nimi]
nimet.reverse()
kaikki_toisinpain = ", ".join(nimet)

print(kaikki)
print(kaikki_toisinpain)