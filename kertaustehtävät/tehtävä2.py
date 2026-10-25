kokonaisluku = int(input("anna kokonaisluku: "))

if kokonaisluku % 3 == 0 and kokonaisluku % 5 == 0:
    print ("Luku on kolmella sekä viidellä jaollinen.")
elif kokonaisluku % 5 == 0:
    print ("Luku on viidellä jaollinen.")
elif kokonaisluku % 3 == 0:
    print ("Luku on kolmella jaollinen.")
elif kokonaisluku %3 != 0 or kokonaisluku %5 != 0:
    print ("Luku ei ole kolmella tai viidellä jaollinen.")