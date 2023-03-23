import Course
import Student
from datetime import date


class Grade:

    def __init__(self, weight: float, datum: date, level: int):
        self.weight = weight
        self.datum = datum
        self.level = level
        self.course = Course
        self.student = Student
