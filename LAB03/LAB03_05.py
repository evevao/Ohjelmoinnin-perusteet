#LAB03 tehtävä 05

#Teksti komennot
print("Anna 5 lukua")
num1 = int(input("Anna 1.luku: "))
num2 = int(input("Anna 2.luku: "))
num3 = int(input("Anna 3.luku: "))
num4 = int(input("Anna 4.luku: "))
num5 = int(input("Anna 5.luku: "))
sum = 0 
       #+ num3 + num4 + num5)

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

print("Lukujen summa on: ", sum)