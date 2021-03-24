with open("tekst2.txt", "w+") as plik:
    plik.write("Ala\nMa\nKota\n")

with open("tekst2.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

