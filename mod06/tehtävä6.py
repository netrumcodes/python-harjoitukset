import math

def pizzainfo(halkaisija, hinta):
    sade = (halkaisija / 100) / 2
    ala = math.pi * (sade ** 2)
    return hinta / ala

# pizza = [halkaisija, hinta]
pizza1 = [float(input("Anna pizzan halkaisija sentteinä: ")),
          float(input("Anna pizzan hinta: "))]
pizza2 = [float(input("Anna toisen pizzan halkaisija sentteinä: ")),
          float(input("Ja tämän pizzan hinta: "))]

if pizzainfo(*pizza1) > pizzainfo(*pizza2):
    print("Toinen pizza antaa rahoille paremman vastineen.")
elif pizzainfo(*pizza1) < pizzainfo(*pizza2):
    print("Ensimmäinen pizza antaa rahoille paremman vastineen.")
else:
    print("Pizzat ovat yhtä edullisia.")