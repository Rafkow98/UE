class Book:
    def __init__(self, library, publication_date, author_name, author_surname,
                 number_of_pages):
        self.library = library
        self.author_name = author_name
        self.author_surname = author_surname
        self.publication_date = publication_date
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Biblioteka: {self.library}. ' \
               f'Data publikacji: {self.publication_date}. ' \
               f'Imię autora: {self.author_name}. ' \
               f'Nazwisko autora: {self.author_surname}. ' \
               f'Liczba stron: {self.number_of_pages}'
