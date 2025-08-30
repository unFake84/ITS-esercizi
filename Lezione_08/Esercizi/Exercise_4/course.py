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
            self.professor = prof

        else:
            raise ValueError(f"The professor: {prof} is already assigned to this course")

    def __str__(self) -> str:
        prof_str: str = str(self.professor.name) if self.professor else 'Not yet assigned'
        student_str: str = '\nSTUDENTS OVERVIEW:\n' + "\n" + \
                            "\n".join([f'[{i}]\n' + str(s) for i, s in enumerate(self.students, 1)]) + \
                            "\nEND STUDENTS OVERVIEW\n" if self.students else ''
        student_len: int = len(self.students) if self.students else 0

        return f"Course name: {self.course_name}\n"\
                f"Course code: {self.course_code}\n"\
                f"Professor: {prof_str}\n"\
                f"Students: {student_len}\n{student_str}"
    
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