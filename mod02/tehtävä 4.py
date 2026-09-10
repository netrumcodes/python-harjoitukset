import math
kokonaisluku1 = int(input("Anna ensimmäinen kokonaisluku: "))
kokonaisluku2 = int(input("Anna toinen kokonaisluku: "))
kokonaisluku3 = int(input("Anna kolmas kokonaisluku: "))
summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = summa / 3
print(f"Kolmen kokonaisluvun summa on {summa}, tulo on {tulo}, ja keskiarvo on {keskiarvo:.2f}")