#LAB06 tehtävä 01

sekunti_input = int(input("Anna sekuntiarvo: "))

h = sekunti_input // 3600
min = (sekunti_input % 3600) // 60
sec = sekunti_input % 60

def showtime():
    print("Tulos: {}:{}:{}".format(h, min, sec))
    return

showtime()