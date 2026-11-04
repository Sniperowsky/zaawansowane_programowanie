from .book import Book
from .employee import Employee
from .student import Student


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
