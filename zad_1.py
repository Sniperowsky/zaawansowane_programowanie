from magazine1 import Student


def main():
    student1 = Student("Bartosiński", [40, 69, 90, 90, 80, 85])
    student2 = Student("Jankowski", [34, 50, 40, 20, 15])

    print(student1.isPassing())
    print(student2.isPassing())


if __name__ == "__main__":
    main()