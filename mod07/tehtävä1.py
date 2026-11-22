vuodenaika = ("talvi", "talvi", 
           "kevät", "kevät", "kevät", 
           "kesä", "kesä", "kesä", 
           "syksy", "syksy", "syksy", "talvi")
numero = int(input("Anna kuukautta vastaava järjestysnumero (1-12): "))
season = vuodenaika[numero-1]
print(f"{numero}. vuodenaika on {season}.")