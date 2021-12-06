import z43_house
import z43_flat

house1 = z43_house.House(123, 5, 400000, "Adres 1", 234)
flat1 = z43_flat.Flat(111, 3, 300000, "Adres 2", 6)
print(house1.__str__())
print(flat1.__str__())
