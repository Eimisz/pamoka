nuo = int(input("iveskite metus nuo: "))
iki = int(input("iveskite metus iki: "))

def keliamieji():
    sarasas = list(range(nuo, iki, 4))
    print(sarasas)

keliamieji()

input("")