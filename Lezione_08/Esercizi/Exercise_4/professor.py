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
        if course.professor is not None:
            err_str: str = f"Can not add professor {self.name} to course {course.course_name}.\n"\
                            f"Professor {course.professor.name} already assigned to this course: {course.course_name}"
            raise ValueError(err_str)

        else:
            # self.courses.append(course) # per responsabilità doppia
            course.professor = self

    def set_department(self, depart: Department) -> None:
        if depart != self.department:
            self.department = depart

        else:
            raise ValueError(f"Professor is already assigned to this department")

    def __str__(self):
        depart_str: str = self.department.department_name if self.department else f"{'Not assigned':<10}"
        courses_str: str = '\n '.join([c.course_name for c in self.courses]) if self.courses else f"{'No courses assigned':<10}"

        return super().__str__() + f"{'ID:':<12} {self.professor_id:<10}\n{'Department:':<12} {depart_str:<10}\n{'Courses:':<12} {courses_str:<10}"