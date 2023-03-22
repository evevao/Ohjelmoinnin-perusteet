#LAB06 tehtävä 04

import random

sum = 0
numero = []

for i in range(5):
   tulos = random.randint(1, 20)
   print("Hypyn pisteet: ", tulos)
   sum += tulos
   sum2 = sum - min(tulos) - max(tulos)
   
   
print("Summa: ", sum2)

#ei toimi