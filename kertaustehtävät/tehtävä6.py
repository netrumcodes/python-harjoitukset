numerolista = []
usernum = int
while usernum != 0:
    usernum = int(input("Anna numero: "))
    numerolista.append(usernum)
    uusilista = sorted(numerolista, reverse=True)
    print(numerolista)
    print(uusilista)