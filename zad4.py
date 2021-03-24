class naZakupy:
    def __init__(self, a, b, c ,d):
        self.nazwa_produktu = a
        self.ilosc = b
        self.jednostka_miary = c
        self.cena_jed = d
    def wyswietl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed
    def ile_produktu(self):
        return str(self.ilosc)+self.jednostka_miary
    def ile_kosztuje(self):
        return self.cena_jed * self.ilosc

zakupy = naZakupy("jabłka", 20, "kg", 2)
print(zakupy.wyswietl_produkt())
print(zakupy.ile_produktu())
print(zakupy.ile_kosztuje())