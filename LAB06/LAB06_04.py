#LAB06 tehtävä 04


#Teksti komennot
num_input = 5
inputs = []
sum = 0

print("Anna alla 5 pisteytystä hypylle.")

#funktio komento
for i in range(num_input):
    user_input = int(input("Hypyn pisteet: "))
    inputs.append(user_input)
    sum = sum + user_input
    maxi = max(inputs)
    mini = min(inputs)

sum2 = (sum - maxi - mini)

print("Pisteet yhteensä:", sum2)