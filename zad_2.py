
class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Księgarnia w mieście {self.city} na ulicy {self.street}. Kod pocztowy {self.zip_code}. Otwarta w godzinach {self.open_hours}. Numer kontaktowy {self.phone}.'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'{self.first_name} {self.last_name}, zatrudniony: {self.hire_date}, data urodzenia: {self.birth_date}, adres: {self.city}, {self.street}, {self.zip_code}, tel. {self.phone}'


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Autor: {self.author_name} {self.author_surname}, '
                f'data publikacji: {self.publication_date}, '
                f'liczba stron: {self.number_of_pages}\n'
                f'Biblioteka: {self.library}')


class Order:
    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = ""

        for book in self.books:
            books_description += f'\n{book}\n'

        return (f'Data zamówienia: {self.order_date}\n'
                f'Pracownik: {self.employee}\n'
                f'Student: {self.student}\n'
                f'Książki: {books_description}')


library1 = Library("Katowice", "Mariacka 10", "40-001", "8:00-18:00", "123456789")
library2 = Library("Kraków", "Szkolna 7", "30-001", "9:00-17:00", "987654321")
book1 = Book(library1, 2000, 'Jan', 'Nowak', 340)
book2 = Book(library2, 1995, 'Genowefa', 'Bartosińska', 550)
book3 = Book(library1, 2016, 'Aleksander', 'Volk', 446)
book4 = Book(library2, 2020, 'Lukas', 'Bermou', 539)
book5 = Book(library1, 1979, 'Andre', 'Botacielli', 346)
employee1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-10", "Katowice", "Polna 5", "40-100", "111222333")
employee2 = Employee("Anna", "Nowak", "2021-03-15", "1995-07-20", "Kraków", "Leśna 8", "30-200", "444555666")
employee3 = Employee("Piotr", "Wiśniewski", "2022-06-01", "1988-02-12", "Katowice", "Długa 3", "40-300", "777888999")
student1 = Student("Adam", "Bartosiński")
student2 = Student("Marek", "Jankowski")
student3 = Student("Kasia", "Zielińska")

order1 = Order(employee1, student1, [book1, book2, book3], "2026-10-21")
order2 = Order(employee2, student2, [book4, book5], "2026-10-22")

print(order1)
print(order2)
