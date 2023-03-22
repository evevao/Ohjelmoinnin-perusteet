#LAB05 tehtävä 02

print("Lasketaan lukujen erotus.")
print("Anna alla kaksi numeroa.")

num1 = int(input("Anna numero: "))
num2 = int(input("Anna toinen numero: "))
tulo = "Numeroiden erotus:"

def subtract():
    return print(tulo, num1 - num2)
subtract()