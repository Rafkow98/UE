class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Imię: {self.first_name}. ' \
               f'Nazwisko: {self.last_name}. ' \
               f'Data zatrudnienia: {self.hire_date}. ' \
               f'Data urodzenia: {self.birth_date}. ' \
               f'Miasto: {self.city}. ' \
               f'Ulica: {self.street}. ' \
               f'Kod pocztowy: {self.zip_code}. ' \
               f'Telefon: {self.phone}'
