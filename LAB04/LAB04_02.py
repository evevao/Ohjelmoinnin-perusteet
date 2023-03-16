#LAB04 tehtävä 02

#Tekstikomennot
print("Anna viikon sademäärä")
num1 = int(input("Anna maanantain sademäärä: "))
num2 = int(input("Anna tiistain sademäärä: "))
num3 = int(input("Anna keskiviikon sademäärä: "))
num4 = int(input("Anna torstain sademäärä: "))
num5 = int(input("Anna perjantain sademäärä: "))
num6 = int(input("Anna lauantain sademäärä: "))
num7 = int(input("Anna sunnuntain sademäärä: "))
sum = 0 

#printti komennot
if num1 >= 1:
    sum = sum + num1
if num2 >= 1:
    sum = sum + num2
if num3 >= 1:
    sum = sum + num3
if num4 >= 1:
    sum = sum + num4
if  num5 >= 1:
    sum = sum + num5
if num6 >= 1:
    sum = sum + num6
if num7 >= 1:
    sum = sum + num7

print("Sademäärä yhteensä: ", sum)