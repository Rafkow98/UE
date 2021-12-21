class Nieruchomosc:
    def __init__(self, powierzchnia, miasto, ulica, nr_budynku, kod_pocztowy, cena_za_m2):
        self.powierzchnia = powierzchnia
        self.miasto = miasto
        self.ulica = ulica
        self.nr_budynku = nr_budynku
        self.kod_pocztowy = kod_pocztowy
        self.cena_za_m2 = cena_za_m2

    @property
    def powierzchnia(self):
        return self.powierzchnia

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

    @property
    def cena_za_m2(self):
        return self.cena_za_m2

    @powierzchnia.setter
    def powierzchnia(self, p):
        self.powierzchnia = p

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

    @cena_za_m2.setter
    def cena_za_m2(self, c):
        self.cena_za_m2 = c
