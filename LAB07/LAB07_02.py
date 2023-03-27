#LAB07 tehtävä 02

name = ""
age = 0

class Human:

    def __str__(self):
        return "Nimi: " + self.name + ", ikä: " + str(self.age)
    
kokonaan1 = Human()
kokonaan1.name = "Kalle"
kokonaan1.age = 14

kokonaan2 = Human()
kokonaan2.name = "Eeva"
kokonaan2.age = 18
    

print(kokonaan1)
print(kokonaan2)