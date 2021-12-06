import library
import book
import employee
import z41_student


class Order:
    def __init__(self, library: library.Library, employee: employee.Employee,
                 student: z41_student.Student, books: book.Book, order_date):
        self.library = library
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Pracownik: {self.employee.first_name} ' \
               f'{self.employee.last_name}. ' \
               f'Student: {self.student.name}.' \
               f' Biblioteka na ulicy: {self.library.street} ' \
               f'w mieście {self.library.city}. ' \
               f'Autor wypożyczonej książki: {self.books.author_name} ' \
               f'{self.books.author_surname}. ' \
               f'Data zamówienia: {self.order_date}'


bib1 = library.Library("Katowice", "Ulica 1", "22-222", "8-16", 123123123)
bib2 = library.Library("Częstochowa", "Ulica 2", "33-333", "9-17", 456456456)

prac1 = employee.Employee("Abc", "Def", "2020-03-03", "1980-02-02",
                          "Miasto1", "Ulica1", "22-222", 123212321)
prac2 = employee.Employee("Ghi", "Jkl", "2010-04-04", "1985-07-03",
                          "Miasto2", "Ulica2", "33-333", 987654321)
prac3 = employee.Employee("Mno", "Pqr", "2015-05-05", "1990-07-08",
                          "Miasto3", "Ulica3", "44-444", 543456789)

ks1 = book.Book("bib1", "2018-02-02", "Aaa", "Bbb", 123)
ks2 = book.Book("bib2", "2020-06-12", "Ccc", "Ddd", 133)
ks3 = book.Book("bib1", "2005-07-07", "Eee", "Fff", 127)
ks4 = book.Book("bib1", "2014-03-30", "Ggg", "Hhh", 256)
ks5 = book.Book("bib2", "2021-04-25", "Iii", "Jjj", 311)

stud1 = z41_student.Student("Aaa Bbb", 50)
stud2 = z41_student.Student("Ccc Ddd", 60)

zam1 = Order(bib1, prac1, stud1, ks1, "12-11-2021")
zam2 = Order(bib2, prac2, stud2, ks2, "18-11-2021")

print(zam1.__str__())
print(zam2.__str__())
