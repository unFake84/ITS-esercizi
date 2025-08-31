'''
    [4]
    Create a class Course:
    Attributes:

        course_name
        course_code
        students (list of Student instances)
        professor (Professor instance)

    Methods:

        add_student, to add a student to the course.
        set_professor, to set the professor for the course.
        __str__, method to return a string representation of the course.

'''


from __future__ import annotations
from student import Student
from professor import Professor

class Course:

    def __init__(self, course_name: str, course_code: str, professor: Professor|None = None) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = professor

    def add_student(self, student: Student) -> None:
        if student not in self.students:

            self.students.append(student)
            student.enroll(self)

        else:
            raise ValueError(f"The student: {student.name} is already enrolled in this course: {self.course_name}")
    
    def set_professor(self, prof: Professor) -> None:
        if prof != self.professor:

            # prof.assign_to_course(self) per doppia responsabilità
            self.professor = prof
            prof.courses.append(self)

        else:
            raise ValueError(f"The professor: {prof} is already assigned to this course")

    def __str__(self) -> str:
        prof_str: str = str(self.professor.name) if self.professor else f'{"Not yet assigned":<10}'

        student_str: str = f'\nSTUDENTS {self.course_name.upper()} OVERVIEW:\n' + "\n" + \
                            "\n".join([f'{"Student " + "-" * 4} [{i}]\n' + str(s) for i, s in enumerate(self.students, 1)]) + \
                            f"\nEND STUDENTS {self.course_name.upper()} OVERVIEW\n" if self.students else ''

        student_len: int = len(self.students) if self.students else 0

        return f"{'Course name:':<12} {self.course_name:<10}\n"\
                f"{'Course code:':<12} {self.course_code:<10}\n"\
                f"{'Professor:':<12} {prof_str:<10}\n"\
                f"{'Students:':<12} {student_len:<10}\n{student_str:<10}"

if __name__ == "__main__":

    print("-"*50)

    mathcourse: Course = Course("Math", "H001")

    student1: Student = Student("Pippo", 49, "AH10B")
    student2: Student = Student("Pluto", 40, "AH14A")
    student3: Student = Student("Clarabella", 39, "AM02D")

    print(mathcourse)
    print("-"*50)

    mathcourse.add_student(student1)
    mathcourse.add_student(student2)
    mathcourse.add_student(student3)

    try:
        mathcourse.add_student(student3)

    except ValueError as err:
        print(f"{err}\n{'-'*50}")

    print(mathcourse)
    print("-"*50)

    # Prima di Department
    #########################################################################