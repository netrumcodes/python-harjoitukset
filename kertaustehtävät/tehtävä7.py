sanat = ["luonto", "puu", "kissa", "mäyräkoira"]
kirjaimet = 0
for a in sanat:
    if len(a) > 5:
        kirjaimet = kirjaimet + 1
print(kirjaimet)