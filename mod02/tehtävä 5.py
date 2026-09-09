leiviskät = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
massa_grammoina = leiviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3
kilogrammat = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000
print(f"Massa on {kilogrammat} kg ja {grammat:.2f} g")