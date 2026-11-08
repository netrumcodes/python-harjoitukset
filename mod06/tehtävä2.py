import random
def noppa(tahko):
    return random.randint(1,tahko)

tahko = int(input("Anna tahkojen määrä: "))
heitto = 0
while heitto != tahko:
    heitto = noppa(tahko)
    print(heitto)
