import Zamowienie
import Deweloper
import Mieszkanie

if __name__ == '__main__':
    d1 = Deweloper.Deweloper("Deweloper 1", "Katowice", "Ulica 1", 44, "22-222")
    m1 = Mieszkanie.Mieszkanie(70, "Częstochowa", "Ulica 2", 12, "33-333", 10000, 4)
    z1 = Zamowienie.Zamowienie()
    z1.id_zamowienia = 1
    z1.data_zamowienia = "21-12-2021"
    z1.deweloper = d1
    z1.mieszkanie = m1
    z1.__str__(z1.id_zamowienia, z1.data_zamowienia, z1.deweloper, z1.mieszkanie)
