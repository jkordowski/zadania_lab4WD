class def_aryt:
    a1 = 0
    r = 0
    n = 0
    ciag = [a1]

    def wyswietl_dane(self):
        return self.ciag

    # def pobierz_elementy(self):

    def pobierz_parametry(self, a1, r , n):
        self.a1 = a1
        self.r = r
        self.n = n

    def policz_sume(self):
        an = self.a1 + (self.n-1) * self.r
        return (self.a1 + an) * self.n/2
    # def policz_elementy(self):

a = def_aryt
