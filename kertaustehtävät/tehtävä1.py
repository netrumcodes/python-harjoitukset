tuntipalkka = int(input("Anna tuntipalkka: "))
tunnit = int(input("Anna tehdyt tunnit: "))
viikonpv = input("Anna viikonpäivä: ")

if viikonpv == "sunnuntai" or viikonpv == "su":
    tuntipalkka = tuntipalkka*2
print (f"päiväpalkkasi on {tuntipalkka*tunnit}")