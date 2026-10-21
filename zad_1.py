
class Student:
    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self.marks = marks

    def isPassing(self) -> bool:
        avg = sum(self.marks) / len(self.marks)

        if avg > 50:
            return True
        else:
            return False


Student1 = Student("Bartosiński", [40, 69, 90, 90, 80, 85])
Student2 = Student("Jankowski", [34, 50, 40, 20, 15])

print(Student1.isPassing())
print(Student2.isPassing())
