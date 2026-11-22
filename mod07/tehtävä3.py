lentoasemat = [
    {
        "nimi": "Helsinki-Vantaa",
        "icao": "EFHK"
    },
    {
        "nimi": "Tallinna",
        "icao": "EETN"
    },
    {
        "nimi": "Frankfurt",
        "icao": "EDDF"
    }
]
select = None

while select != 3:
    print("Valitse toiminto:")
    print("1. Hae lentoasema")
    print("2. Syötä uuden lentoaseman tiedot")
    print("3. Keskeytä ohjelma")
    select = int(input(""))
    if select == 1:
        usericao = input("Anna lentoaseman ICAO-koodi: ")
        for asema in lentoasemat:
            if asema["icao"] == usericao:
                print(asema["nimi"])
                break
        else:
            print("Lentoasemaa ei löytynyt.")
    elif select == 2:
        uusi_nimi = input("Anna lentoaseman nimi: ")
        uusi_icao = input("Anna lentoaseman ICAO-koodi: ")
        lentoasemat.append({"icao": uusi_icao, "nimi": uusi_nimi})
        print(f"Lentoasema {uusi_nimi} on lisätty tietokantaan.")
print("Ohjelma päätetty.")