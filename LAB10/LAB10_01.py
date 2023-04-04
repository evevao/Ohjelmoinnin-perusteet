#LAB10 tehtävä 01

import datetime


try:
    annettuIka = int(input("Anna syntymävuotesi: "))
    paivaNyt = datetime.datetime.today()
    vuosiNyt = int(paivaNyt.year)
    laskettuIka = (vuosiNyt - annettuIka)
    print("Ikäsi on:", laskettuIka, "vuotta.")
    if laskettuIka <= 1:
        print("Vauva.")
    elif laskettuIka <= 13:
        print("Lapsi.")
    elif laskettuIka <= 19:
        print("Teini.")
    elif laskettuIka <= 65:
        print("Aikuinen.")
    else: 
        print("Seniori.")
except ValueError:
    print("Annettu syöttö ei ollut luku. koita uudelleen.")