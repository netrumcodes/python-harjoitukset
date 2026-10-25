tarina = ""
aiempi = ""
userinput = input("Anna sana tarinaan: ")
while userinput != "loppu" and userinput != aiempi:
    tarina = tarina + userinput + " "
    aiempi = userinput
    userinput = input("Anna sana tarinaan: ")
print(tarina)

