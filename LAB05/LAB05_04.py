#LAB05 tehtävä 04

#teksti komennot
ajettu = float(input("Anna ajettu kilometrimäärä: "))
keskikulutus = float(input("Anna keskikulutus 100km kohti: "))
summa = "Kulutus:"

#funktio komento
def get_fuel():
    return print(summa, str(round((ajettu*(keskikulutus/100)), 1)), "ltr")
get_fuel()