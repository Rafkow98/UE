import Nieruchomosc


class Dom(Nieruchomosc):
    def __init__(self, powierzchnia, miasto, ulica, nr_budynku, kod_pocztowy, cena_za_m2, powierzchnia_ogrodu):
        super().__init__(powierzchnia, miasto, ulica, nr_budynku, kod_pocztowy, cena_za_m2)
        self.powierzchnia_ogrodu = powierzchnia_ogrodu

    @property
    def powierzchnia_ogrodu(self):
        return self.powierzchnia_ogrodu
