class Deweloper:
    def __init__(self, nazwa, miasto, ulica, nr_budynku, kod_pocztowy):
        self.nazwa = nazwa
        self.miasto = miasto
        self.ulica = ulica
        self.nr_budynku = nr_budynku
        self.kod_pocztowy = kod_pocztowy

    @property
    def nazwa(self):
        return self.nazwa

    @property
    def miasto(self):
        return self.miasto

    @property
    def ulica(self):
        return self.ulica

    @property
    def nr_budynku(self):
        return self.nr_budynku

    @property
    def kod_pocztowy(self):
        return self.kod_pocztowy

    @nazwa.setter
    def nazwa(self, n):
        self.nazwa = n

    @miasto.setter
    def miasto(self, m):
        self.miasto = m

    @ulica.setter
    def ulica(self, u):
        self.miasto = u

    @nr_budynku.setter
    def nr_budynku(self, nr):
        self.nr_budynku = nr

    @kod_pocztowy.setter
    def kod_pocztowy(self, k):
        self.kod_pocztowy = k

    def __str__(self, nazwa, miasto, ulica, nr_budynku, kod_pocztowy):
        return f'Nazwa: {self.nazwa}, Miasto: {self.miasto}, Ulica: {self.ulica}' \
               f'Numer budynku: {self.nr_budynku}, Kod pocztowy: {self.kod_pocztowy}'
