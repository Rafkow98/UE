import Nieruchomosc


class Mieszkanie(Nieruchomosc):
    def __init__(self, powierzchnia, miasto, ulica, nr_budynku, kod_pocztowy, cena_za_m2, nr_pietra):
        super().__init__(powierzchnia, miasto, ulica, nr_budynku, kod_pocztowy, cena_za_m2)
        self.nr_pietra = nr_pietra

    @property
    def nr_pietra(self):
        return self.nr_pietra
