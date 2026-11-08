def summa(num):
    s = 0
    for n in num:
        s += n
    return s

numerot = [1,2,3,4,5]
print("listan numeroiden summa on ", summa(numerot))