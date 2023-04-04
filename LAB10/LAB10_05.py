#LAB10 tehtävä 05

import os.path
import datetime

tiedostoReitti = os.path.expanduser("~")
print("Kotihakemisto on ", tiedostoReitti)

try: 
    tiedostonNimi = "ayho.txt"
    tiedostoReitti += "\\"
    tiedosto = open(tiedostoReitti + tiedostonNimi, "w")
    teksti = "Tiedosto " + tiedostonNimi + " luotu onnistuneesti." + str(datetime.datetime.now())
    tiedosto.write(teksti + "\n" + "*Tässä on nyt jotain muutakin tekstiä, jotta se ei olisi niin tyhjä.*"+ "\n" + ":)")
    tiedosto.close()
    print(teksti)
except:
    print("Tiedostoa " + tiedostonNimi + " luoda.")