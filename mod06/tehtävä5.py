def listaconverter(lista):
    muunnettu = []    
    for l in lista:
        if l % 2 !=0:
            muunnettu.append(l)
    return muunnettu

lukuja = [42,2,12,98,3,4,6,5,75,43]

print("tässä alkuperäinen lista: ", lukuja)
print("tässä sama lista, josta poistettu kahdella jaolliset: ", listaconverter(lukuja))
