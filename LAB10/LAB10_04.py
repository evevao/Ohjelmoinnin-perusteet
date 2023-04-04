#LAB10 tehtävä 04

nameslist = {}
key = 0
tiedostonNimi = "names.txt"

try: 
    with open("names.txt", "r") as tiedosto:
        for name in tiedosto:
            nameslist[key] = name
            value = name.split()
            key = key + 1
        print(f"Tiedosto {tiedostonNimi} luettu.")
        longestName = ""
        for value in nameslist.values():
            if len(value) > len(longestName):
                longestName = value
except:
    print(f"Tiedostoa {tiedostonNimi} ei voitu lukea.")

print("Listassa on", key, "nimeä.")
print("Pisin nimi on:", longestName)
tiedosto.close()