tuotteet = []
amount = []
cont = "Kyllä"
while cont == "Kyllä":
    tuotteet.append(input("Mitä tuotetta valmistetaan? "))
    amount.append(int(input("Monta tuotetta valmistetaan? ")))
    cont = input("Jatketaanko tuotantoa? ")
    while cont not in ("Kyllä", "Ei"):
        print("Vastaa Kyllä tai Ei.")
        cont = input("Jatketaanko tuotantoa? ")

print()
print("Tuotanto lopetettu!")
print()
print("Valmistetut tuotteet:")
for a in range(len(tuotteet)):
    print(f"{tuotteet[a]}: {amount[a]}")