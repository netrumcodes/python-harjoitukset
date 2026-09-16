#Tehtävä 2

print("Muunna tuumat senttimetreiksi.")
inch = 0
while inch >= 0:
    inch = float(input("Syötä tuumat: "))
    cm = inch * 2.54
    print(f"{inch} tuumaa on {cm} senttimetriä.")
print("Arvo negatiivinen, ohjelma keskeytetty.")