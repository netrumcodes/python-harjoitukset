#Tehtävä 3

user = "tyhjä"
numerot = []

while user != "":
    user = (input("Syötä numero: "))
    if user != "":
        numerot.append(int(user))
print(min(numerot))
print(max(numerot))