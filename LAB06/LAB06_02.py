#LAB06 tehtävä 02

#Teksti komennot
selvennys = input("Anna aste selvennys C tai F: ")
aste = int(input("Anna astearvo: "))


#funktio komennot
def celToFah():
    if selvennys == "C":
        print("Muutettu astearvo:", round(((aste * 9/5) + 32), 1), "F")
    return  
celToFah()


def fahToCel():
    if selvennys == "F":
        print("Muutettu astearvo:", round(((aste - 32) *5/9), 1), "C")
    return
fahToCel()