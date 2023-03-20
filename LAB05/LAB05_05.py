#LAB05 tehtävä 05

#teksti komennot
ajettu = float(input("Anna ajetut kilometrit: "))
keskikulutus = float(input("Anna keskikulutus 100km kohti: "))
litrat = float(input("Anna polttoaineen litrahinta: "))

#funktio komento
def get_cost():
    return print("Kustannukset:",str(round((ajettu*(keskikulutus/100)*litrat), 2)),"€")
get_cost()