#LAB10 tehtävä 04

nameslist = {}
key = 0
try: 
    with open("names.txt", "r") as tiedosto:
        for name in tiedosto:
            nameslist[key] = name
            value = name.split()
            key = key + 1
        print("Tiedosto names.txt luettu.")
        longestName = ""
        for value in nameslist.values():
            if len(value) > len(longestName):
                longestName = value
except TypeError:
    pass

print("Listassa on", key, "nimeä.")
print("Pisin nimi on:", longestName)