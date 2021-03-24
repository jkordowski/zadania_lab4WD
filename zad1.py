import sys
plik = open("tekst.txt", "w+")
# lista = []
for x in range(31):
    plik.write(str(x*2)+"\n")
    # lista += [x*2]
# plik.writelines(str(lista))
plik.close()
