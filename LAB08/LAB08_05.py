#LAB08 tehtävä 05

import random


def lotto():
    numerot = [random.randint(1, 40) for _ in range(7)]
    numerot_str = ", ".join(map(str, numerot))
    return numerot_str
print(lotto())