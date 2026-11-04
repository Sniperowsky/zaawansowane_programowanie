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
