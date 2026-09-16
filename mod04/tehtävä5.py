#Tehtävä 5

username = str("pyyttoni")
password = str("äyskäri")
input1 = str("")
input2 = str("")

while input1 != username or input2 != password:
    input1 = input("Anna käyttäjätunnus: ")
    input2 = input("Anna salasana: ")
    if input1 != username or input2 != password:
        print("Pääsy evätty")
    if input1 == username and input2 == password:
        print("Tervetuloa")