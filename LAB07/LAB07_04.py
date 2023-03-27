#LAB07 tehtävä 04

class Mobile:
    def __init__(self, brand="", model="", price=0):
        self.brand = brand
        self.model = model
        self.price = price

brand = ""
model = ""
price = 0

phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(phone1.brand, phone1.model, "is", phone1.price, "€")
print(phone2.brand, phone2.model, "is", phone2.price, "€")