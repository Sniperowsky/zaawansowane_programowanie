from magazine import Book, Employee, Library, Order, Student


def main():
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


if __name__ == "__main__":
    main()
