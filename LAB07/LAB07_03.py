#LAB07 tehtävä 03


class Cat:
    name = ""
    colour = ""

    def miau(self):
        return "says: Meoooooow!"

    def __init__(self, name="", colour=""):
        self.name = name
        self.colour = colour

    def __str__(self):
        return self.name + ", colour: " + self.colour
    
    name = ""
    colour = ""

cat1 = Cat()
cat1.name = "Kit"
cat1.colour = "black"

cat2 = Cat()
cat2.name = "Kat"
cat2.colour = "white"
    

print(cat1)
print(cat2)
print(cat1.name, cat1.miau())
print(cat2.name, cat2.miau())