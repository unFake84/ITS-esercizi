'''
    [3]
    Create subclass Professor that inherit from Person and implement the abstract method.
    Class Professor:
    Additional attributes:

            professor_id,
            department (a Department instance), 
            courses (list of Course instances)

    Additional method:

            assign_to_course, to assign the professor to a course.
            set_department, to assign the professor to the department.

'''

from __future__ import annotations
from person import Person

class Professor(Person):

    def __init__(self, name, age, professor_id: str, department: Department) -> None:
        super().__init__(name, age)

        self.professor_id = professor_id
        self.department = department
        self.courses: list[Course] = []

    def get_role(self) -> str:
        return "Professor"

    def assign_to_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

        else:
            raise ValueError(f"Professor {self.name} already assigned to this the course: {course}")

    def set_department(self, depart: Department) -> None:
        if depart != self.department:
            self.department = depart

        else:
            raise ValueError(f"Professor is already assigned to this department")

    def __str__(self):
        depart_str: str = self.department.department_name if self.department else "Not assigned"
        courses_str: str = '\n '.join([c.course_name for c in self.courses]) if self.courses else "No courses assigned"

        return super().__str__() + f"ID: {self.professor_id}\nDepartment: {depart_str}\nCourses: {courses_str}"