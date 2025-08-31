'''
    [6]
    Create a class University:

    Attributes:

        name
        departments (list of Department instances)
        students (list of Student instances)

    Methods:

        add_department, to add a department to the university.
        add_student, to add a student to the university.
        __str__, method to return a string representation of the university.

'''

from __future__ import annotations
from person import Person
from student import Student
from professor import Professor
from course import Course
from department import Department

class University:

    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: list[Department] = []
        self.students: list[Student] = []

    def add_department(self, n_depart: Department) -> None:
        if n_depart not in self.departments:
            self.departments.append(n_depart)

        else:
            raise ValueError(f"Department {n_depart.department_name} allready exist")

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)

        else:
            raise ValueError(f"Student {student.name} already enrolled at this university")

    def __str__(self) -> str:
        final_string: str = f"\t\t\tUniversity: {self.name}\n\n"
        if not self.departments:
            final_string += "No departments in this university"

        else:
            final_string += f"\n{'Departments:':<8} {len(self.departments):<10}\n\n"

            for i, dptm in enumerate(self.departments, 1):

                final_string += f"[{i}]\n" + str(dptm) + "\n\n"

        if not self.students:
            final_string += "\n\nNo students registered"

        else:
            final_string += f"\n\n{'Students:':<13} {len(self.students):<10}\n\n"

            for i, stds in enumerate(self.students, 1):

                final_string += f"Student {'-' * 4} [{i}]\n" + str(stds) + "\n"

        return final_string


if __name__ == "__main__":

    university1: University = University("Uni1")

    print(university1)
    print("-"*100)

    department1: Department = Department("Dipartimento1")
    department2: Department = Department("Dipartimento2")
    department3: Department = Department("Dipartimento3")
    university1.add_department(department1)
    university1.add_department(department2)
    university1.add_department(department3)

    course1: Course = Course("Corso1", "0001")
    course2: Course = Course("Corso2", "0002")
    department1.add_course(course1)
    department1.add_course(course2)

    professor1: Professor = Professor("Baudo", 60, "ZZ001AA", department1)
    professor2: Professor = Professor("Corrado", 63, "ZZ057DB", department1)
    department1.add_professor(professor1)
    department1.add_professor(professor2)

    student1: Student = Student("Pippo", 49, "AH10B")
    student2: Student = Student("Pluto", 40, "AH14A")
    student3: Student = Student("Clarabella", 39, "AM02D")
    student4: Student = Student("Paperoga", 31, "AI01F")
    student5: Student = Student("Topolina", 28, "AF08A")
    student6: Student = Student("Paperino", 30, "MN89Z")
    student7: Student = Student("Gastone", 29, "AA000A")
    university1.add_student(student1)
    university1.add_student(student2)
    university1.add_student(student3)
    university1.add_student(student4)
    university1.add_student(student5)
    university1.add_student(student6)
    university1.add_student(student7)
    course1.add_student(student1)
    course1.add_student(student2)
    course1.add_student(student3)
    course1.set_professor(professor1)

    # try:
    #     professor1.assign_to_course(course1)

    # except ValueError as err:
    #     print(err)

    print(university1)
    print("-"*100)