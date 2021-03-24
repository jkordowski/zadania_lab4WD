class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y = self.y + int(ile_krokow) * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y = self.y - int(ile_krokow) * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - int(ile_krokow) * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + int(ile_krokow) * self.krok

    def pokaz_gdzie_jestes(self):
        return self.x, self.y

robak = Robaczek(0,0,1)
robak.idz_w_lewo(4)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_gore(12)
robak.idz_w_prawo(6)
print(robak.pokaz_gdzie_jestes())
robak.idz_w_dol(20)
print(robak.pokaz_gdzie_jestes())
