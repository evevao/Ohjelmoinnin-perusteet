#LAB07 tehtävä 05

class Car:
    def __init__(self, brand="", model="", price=0):
        self.brand = brand
        self.model = model
        self.price = price

brand = ""
model = ""
price = 0

auto1 = Car("Skoda", "Octavia", 3000)
auto2 = Car("Audi", "A4", 4000)
auto3 = Car("Volvo", "V70", 5000)
sum = auto1.price + auto2.price + auto3.price

print("Auto 1:", auto1.brand, auto1.model + ".", "Hinta:", auto1.price, "€")
print("Auto 2:", auto2.brand, auto2.model + ".", "Hinta:", auto2.price, "€")
print("Auto 3:", auto3.brand, auto3.model + ".", "Hinta:", auto3.price, "€")
print("Autojen hinta yhteensä:", sum, "€")