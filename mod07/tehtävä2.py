nimet = set()
userinput = None
while userinput != "":
    userinput = input("Anna nimi: ")
    if userinput == "":
        break
    if userinput in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
    nimet.add(userinput)
    
for n in nimet:
    print(n)