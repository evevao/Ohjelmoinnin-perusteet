#LAB08 tehtävä 04

autotalli = {
    'ABC-123': "Skoda",
    'GHT-456': "Toyota",
    'VHT-587': "Mazda",
    'LDK-761': "Renault",
    'HAH-183': "Mitsubishi",
    'RLI-436': "Kia",
    'OLF-844': "Skoda",
    'FUH-846': "Suzuki",
    'JPG-546': "Volkswagen",
    'AHT-496': "Audi",
    'CRL-404': "Nissan"
}

jarjestys = sorted(autotalli.items())

for key, value in jarjestys:
    print(f"{key}: {value}")