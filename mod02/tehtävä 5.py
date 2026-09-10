leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
massa_grammoina = leiviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3
kilogrammat = massa_grammoina // 1000
grammat = massa_grammoina % 1000
print(f"Massa on {kilogrammat} kg ja {grammat:.2f} g")