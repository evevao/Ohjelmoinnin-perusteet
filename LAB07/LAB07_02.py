#LAB07 tehtävä 02


class Human:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return "Nimi: " + self.name + ", ikä: " + str(self.age)
    
    name = ""
    age = 0

kokonaan1 = Human("Kalle", 14)
kokonaan2 = Human("Eeva", 18)
    

print(kokonaan1)
print(kokonaan2)