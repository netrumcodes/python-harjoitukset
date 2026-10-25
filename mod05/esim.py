ostoslista = ['leipä','voi','päärynä','kana']

tuote = input("Anna tuote: ")

while ostoslista != '':
    if tuote not in ostoslista:
        print ("tuotetta ei ole listassa")
        
    else:
        ostoslista.remove(tuote)
        print(ostoslista)
        tuote = input("Anna tuote: ")
print ("Ostokset suoritettu!")
