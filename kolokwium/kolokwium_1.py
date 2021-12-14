class Produkt:
    def __init__(self, id_produktu: int, produkt: str, kategoria: str, producent: str, cena: float):
        self.id_produktu = id_produktu
        self.produkt = produkt
        self.kategoria = kategoria
        self.producent = producent
        self.cena = cena

    @property
    def id_produktu(self):
        return self.id_produktu

    @property
    def produkt(self):
        return self.produkt

    @property
    def kategoria(self):
        return self.kategoria

    @property
    def producent(self):
        return self.producent

    @property
    def cena(self):
        return self.cena

    def __str__(self):
        return f'ID produktu: {self.id_produktu}, ' \
               f'Produkt: {self.produkt}, ' \
               f'Kategoria: {self.kategoria}, ' \
               f'Producent: {self.producent}, ' \
               f'Cena: {self.cena}'


class Magazyn:
    def __init__(self, id_magazynu: int, miasto: str, ulica: str, nr_budynku: int, kod_pocztowy: str):
        self.id_magazynu = id_magazynu
        self.miasto = miasto
        self.ulica = ulica
        self.nr_budynku = nr_budynku
        self.kod_pocztowy = kod_pocztowy

        @property
        def id_magazynu(self):
            return self.id_magazynu

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

        def __str__(self):
            return f'ID magazynu: {self.id_magazynu}, ' \
                   f'Miasto: {self.miasto}, ' \
                   f'Ulica: {self.ulica}, ' \
                   f'Numer budynku: {self.nr_budynku}, ' \
                   f'Kod pocztowy: {self.kod_pocztowy}'


class Klient:
    def __init__(self, miasto: str, ulica: str, nr_budynku: int, kod_pocztowy: str):
        self.miasto = miasto
        self.ulica = ulica
        self.nr_budynku = nr_budynku
        self.kod_pocztowy = kod_pocztowy

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

    def __str__(self):
        return f'Miasto: {self.miasto}, ' \
               f'Ulica: {self.ulica}, ' \
               f'Numer budynku: {self.nr_budynku}, ' \
               f'Kod pocztowy: {self.kod_pocztowy}'


class KlientDetaliczny(Klient):
    def __init__(self, imie: str, nazwisko: str, miasto: str, ulica: str,
                 nr_domu: int, kod_pocztowy: str, data_urodzenia: str):
        super().__init__(miasto, ulica, nr_domu, kod_pocztowy)
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia

        @property
        def imie(self):
            return self.imie

        @property
        def nazwisko(self):
            return self.nazwisko

        @property
        def data_urodzenia(self):
            return self.data_urodzenia

        def __str__(self):
            return f'Imię: {self.imie}, ' \
                   f'Nazwisko: {self.nazwisko}, ' \
                   f'Data urodzenia: {self.data_urodzenia}, ' \
                   f'Miasto: {self.miasto}, ' \
                   f'Ulica: {self.ulica}, ' \
                   f'Numer budynku: {self.numer_budynku}'


class KlientBiznesowy(Klient):
    def __init__(self, nazwa_firmy: str, miasto: str, ulica: str, nr_domu: int, kod_pocztowy: str):
        super().__init__(miasto, ulica, nr_domu, kod_pocztowy)
        self.nazwa_firmy = nazwa_firmy

        @property
        def nazwa_firmy(self):
            return self.nazwa_firmy

        def __str__(self):
            return f'Nazwa firmy: {self.nazwa_firmy}, ' \
                   f'Miasto: {self.miasto}, ' \
                   f'Ulica: {self.ulica}, ' \
                   f'Numer budynku: {self.numer_budynku}'

class Zamowienie:
        @property
        def id_zamowienia(self):
            return self.id_zamowienia

        @id_zamowienia.setter
        def id_zamowienia(self, id):
            self.id_zamowienia = id

        @property
        def data_zamowienia(self):
            return self.data_zamowienia

        @data_zamowienia.setter
        def data_zamowienia(self, data):
            self.data_zamowienia = data

        @property
        def produkt(self):
            return self.produkt

        @produkt.setter
        def produkt(self, prod):
            self.produkt = prod

        @property
        def magazyn(self):
           return self.magazyn

        @magazyn.setter
        def magazyn(self, mag):
            self.magazyn = mag

        @property
        def klient(self):
            return self.klient

        @klient.setter
        def klient(self, kl):
            self.klient = kl

        def __str__(self):
            return f'ID zamówienia: {self.id_zamowienia}, ' \
                   f'Data zamówienia: {self.data_zamowienia}, ' \
                   f'Produkt: {self.produkt}, ' \
                   f'Magazyn: {self.magazyn}, ' \
                   f'Klient: {self.klient}'


if __name__ == '__main__':
    produkt1 = Produkt(123, "Telewizor 1", "Telewizory", "LG", 2199.99)
    magazyn1 = Magazyn(21, "Katowice", "Ulica 2", 43, "33-333")
    klient1 = Klient("Częstochowa", "Królewska", 12, "42-202")
    zamowienie1 = Zamowienie()
    zamowienie1.id_zamowienia = 1
    zamowienie1.data_zamowienia = '14-12-2021'
    zamowienie1.produkt = produkt1
    zamowienie1.klient = klient1
    zamowienie1.magazyn = magazyn1
    print(zamowienie1.klient)




