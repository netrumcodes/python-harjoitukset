#Tehtävä4

import random
rnd = int(random.randint(1,10))
usernum = 11
while rnd != usernum:
    usernum = int(input("Syötä lukusi: "))
    if usernum > rnd:
        print(f"Lukusi {usernum} on liian suuri.")
    elif usernum < rnd:
        print(f"Lukusi {usernum} on liian pieni.")
    elif usernum == rnd:
        print(f"Lukusi {usernum} on oikea!")




