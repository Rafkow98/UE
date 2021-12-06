import z43_property


class Flat(z43_property.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f'Mieszkanie o powierzchni {self.area}, '
                f'{self.rooms} pokojach, cenie {self.price}, '
                f'adresie {self.address} i {self.floor} piętrach')
