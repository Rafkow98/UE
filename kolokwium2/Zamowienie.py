import Deweloper
import Nieruchomosc
import Dom
import Mieszkanie


class Zamowienie:
    @property
    def id_zamowienia(self) -> int:
        return self.id_zamowienia

    @property
    def data_zamowienia(self) -> str:
        return self.data_zamowienia

    @property
    def deweloper(self) -> Deweloper:
        return self.deweloper

    @property
    def nieruchomosc(self) -> Nieruchomosc:
        return self.nieruchomosc

    @property
    def dom(self) -> Dom:
        return self.dom

    @property
    def mieszkanie(self) -> Mieszkanie:
        return self.mieszkanie

    @id_zamowienia.setter
    def id_zamowienia(self, id_zam):
        self.id_zamowienia = id_zam

    @data_zamowienia.setter
    def data_zamowienia(self, d):
        self.data_zamowienia = d

    @deweloper.setter
    def deweloper(self, d):
        self.deweloper = d

    @nieruchomosc.setter
    def nieruchomosc(self, n):
        self.nieruchomosc = n

    @dom.setter
    def dom(self, d):
        self.dom = d

    @mieszkanie.setter
    def mieszkanie(self, m):
        self.mieszkanie = m

    def __str__(self, id_zamowienia, data_zamowienia, deweloper, nieruchomosc):
        return f'ID zamówienia: {self.id_zamowienia}, Data zamówienia: {self.data_zamowienia}, ' \
               f'Deweloper: {self.deweloper.nazwa}, Nieruchomość: {self.mieszkanie}'
