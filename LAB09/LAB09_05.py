#LAB09 tehtävä 05

import random

kuinkaMonta = int(input("Kuinka monta lotto riviä?: "))

with open("lotto.txt", "w") as tiedosto:
    for i in range(kuinkaMonta):
        lottorivit = []
        
        while len(lottorivit) < 7:
            numerot = random.randint(1, 40)
            if numerot not in lottorivit:
                lottorivit.append(numerot)
        lottorivit.sort()

        riviMuotoilu = ",".join(str(lotto) for lotto in lottorivit)
        tiedosto.write(riviMuotoilu + "\n")

print(f"{kuinkaMonta} lotto riviä arvottu ja tallennettu tiedostoon 'lotto.txt'.")