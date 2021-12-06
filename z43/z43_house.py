import z43_property


class House(z43_property.Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return(f'Dom o powierzchni {self.area}, {self.rooms} pokojach, '
               f'cenie {self.price}, adresie {self.address} '
               f'i rozmiarze działki {self.plot}')
