#LAB06 tehtävä 05

#Teksti komennot
selvennys = input("Anna mitta selvennys tuuma tai cm: ")
aste = int(input("Anna muunnettava mitta: "))


#funktio komennot
def CmToIn():
    if selvennys == "cm":
        print(aste, "cm on", round(((aste / 2.54)), 2), "tuumaa")
    return  
CmToIn()


def InToCm():
    if selvennys == "tuuma":
        print(aste, "tuumaa on", round(((aste * 2.54)), 2), "cm")
    return
InToCm()