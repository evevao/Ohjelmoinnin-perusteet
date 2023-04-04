#LAB10 tehtävä 02

print("Anna alla karkausvuoden vuosiluku.")

try: 
    annettuVuosi = int(input("Anna vuosiluku: "))
    if annettuVuosi % 4 == 0:
         print("Annettu vuosiluku on karkausvuosi.")
    elif annettuVuosi % 400 == 0:
        print("Annettu vuosiluku on karkausvuosi.")
    else:
        print("Annettu vuosiluku ei ole karkausvuosi.")
except ValueError:
    print("Annettu syöte ei ole luku tai sitä ei voitu laskea.")