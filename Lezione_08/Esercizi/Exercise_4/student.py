'''
    [2]
    Create subclasses Student and that inherit from Person and implement the abstract method.

    Class Student:
    Additional attributes:

            student_id,
            courses (list of Course instances).

    Additional method:

            enroll, to enroll the student in a course.

'''

from __future__ import annotations
from person import Person

class Student(Person):

    def __init__(self, name, age, student_id: str) -> None:
        super().__init__(name, age)

        self.student_id = student_id
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return "Student"

    def enroll(self, n_course: Course) -> None:
        if n_course not in self.courses:

            self.courses.append(n_course)

        else:
            raise ValueError(f"Student is already enrolled in this course: {n_course}")

    def __str__(self):
        course_str: str = ', '.join([c.course_name for c in self.courses]) if self.courses else f"{'No courses yet':<10}"

        return super().__str__() + f"{'ID: ':<12} {self.student_id:<10}\n{'Courses:':<12} {course_str:<10}\n"