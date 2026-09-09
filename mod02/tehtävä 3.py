import math
suorakulmion_kanta = float(input("Anna suorakulmion kanta: "))
suorakulmion_korkeus = float(input("Anna suorakulmion korkeus: "))
suorakulmion_pinta_ala = suorakulmion_kanta * suorakulmion_korkeus
print(f"Suorakulmion pinta-ala on: {suorakulmion_pinta_ala:.2f}")
suorakulmion_piiri = 2 * (suorakulmion_kanta + suorakulmion_korkeus)
print(f"Suorakulmion piiri on: {suorakulmion_piiri:.2f}")