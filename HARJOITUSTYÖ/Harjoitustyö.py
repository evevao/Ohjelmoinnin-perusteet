#Harjoitustyönä teen yksinkertaisen laskimen.

dump = input("Paina Enter-painiketta aloittaaksesi.")

print("Laskin toimii toiminnoilla:")
print("+ = plussa")
print("- = miinus")
print("* = kertomerkki")
print("/ = jakomerkki")
print("** = potenssi")

dump = input("Paina Enter-painiketta jatkaaksesi.")


def plussa(x, y):
    return x + y
def miinus(x, y):
    return x - y
def kertaa(x, y):
    return x * y
def jako(x, y):
    return x / y
def potenssi(x,y):
    return x**y

while True: 
    try: 
        numero1 = float(input("Anna ensimmäinen luku: "))
        break
    except ValueError:
        print("Antamasi merkki ei ollut numero, anna numero.")
        continue

laskutoiminto = input("Anna laskutoimituksen merkki: ")

while True:
    try:
        numero2 = float(input("Anna toinen luku: "))
        break
    except ValueError:
        print("Antamasi merkki ei ollut numero, anna numero.")
        continue

try: 
    if laskutoiminto == "+":
        print(f"{numero1} + {numero2} = {plussa(numero1, numero2)}")
    elif laskutoiminto == "-":
        print(f"{numero1} - {numero2} = {miinus(numero1, numero2)}")
    elif laskutoiminto == "*":
        print(f"{numero1} * {numero2} = {kertaa(numero1, numero2)}")
    elif laskutoiminto == "/":
        print(f"{numero1} / {numero2} = {jako(numero1, numero2)}")
    elif laskutoiminto == "**":
        print(f"{numero1} ** {numero2} = {potenssi(numero1, numero2)}")
    else:
        print("Laskutoimintoa ei voitu suorittaa.")
except TypeError:
    print("Antamasi merkki ei ollut toimiva merkki.")
except ValueError:
    print("Antamasi merkki ei ollut toimiva merkki.")

dump = input("Paina Enter-painiketta lopettaaksesi.")
print("Kiitos, tervetuloa uudelleen.")