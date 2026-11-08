def gallonalitraksi(gallon):
    return gallon * 3.785

user = float(input("anna gallonat: "))
while user >= 0:
    litrat = gallonalitraksi(user)
    print(user, "galloonaa on", litrat, "litraa")
    user = float(input("anna gallonat: "))
