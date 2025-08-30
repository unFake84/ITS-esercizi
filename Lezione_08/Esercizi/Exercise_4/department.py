'''
    [5]
    Create a class Department:

    Attributes:

        department_name
        courses (list of Course instances)
        professors (list of Professor instances)

    Methods:

        add_course, to add a course to the department.
        add_professor, to add a professor to the department.
        __str__, method to return a string representation of the department.

'''

from course import Course
from professor import Professor
from student import Student

class Department:

    def __init__(self, department_name: str) -> None:
        self.department_name = department_name
        self.courses = []
        self.professors = []

    def add_course(self, n_nourse: Course) -> None:
        if n_nourse not in self.courses:
            self.courses.append(n_nourse)
        
        else:
            raise ValueError(f"Course {n_nourse.course_name} not added, already in the system")
    
    def add_professor(self, prof: Professor) -> None:
        if prof not in self.professors:
            self.professors.append(prof)
        
        else:
            raise ValueError(f"Professor {prof} is already present in this department")

    def __str__(self) -> str:
        courses_str: str = '\nCOURSES OVERVIEW:\n' + "\n" + \
            "\n\n".join([f'[{i}]\n' + str(c) for i, c in enumerate(self.courses, 1)]) + \
                "\nEND COURSES OVERVIEW\n" if self.courses else 'No courses yet'

        profs_str: str = 'PROFESSORS OVERVIEW:\n' + "\n" + \
            "\n\n".join([f'[{i}]\n' + str(p) for i, p in enumerate(self.professors, 1)]) + \
                 "\nEND PROFESSORS OVERVIEW\n" if self.professors else 'No associate professors'

        qnti_cors: int = len(self.courses) if self.courses else 0
        qnti_prof: int = len(self.professors) if self.professors else 0

        return f"Department name: {self.department_name}\n"\
                f"Courses: {qnti_cors}\n"\
                f"Professors: {qnti_prof}\n{courses_str}\n{profs_str}"

if __name__ == "__main__":

    print("-"*100 + "\n", "Created: department1", "\n" + "-"*100)
    department1: Department = Department("Dipartimento 1")

    print("DEPARTMENT OVERVIEW\n")
    print(department1)
    #print("-"*50 + '\n')

    print("-"*100 + "\n""Created: course_1\nCreated: professor1", "\n" + "-"*100)
    course_1: Course = Course("Math", "H001")
    professor1: Professor = Professor("Baudo", 60, "ZZ001AA", department1)
    print("COURSE_1 OVERVIEW\n")
    print(course_1)
    print("-"*30)
    print("PROFESSOR_1 OVERVIEW\n")
    print(professor1)

    print("-"*100 + "\n""Added: course_1 to department1\nAdded: professor_1 to department1\nAdded: course_1 to professor1", "\n" + "-"*100)
    department1.add_course(course_1)
    department1.add_professor(professor1)
    professor1.assign_to_course(course_1)

    print("DEPARTMENT OVERVIEW\n")
    print(department1)
    print("-"*100)
    print("COURSE_1 OVERVIEW\n")
    print(course_1)
    print("-"*100)
    print("PROFESSOR_1 OVERVIEW\n")
    print(professor1)

    print("-"*100 + "\n""Created: professor2\nAdded: professor2 to department1 <- Failure expeted", "\n" + "-"*100)
    professor2: Professor = Professor("Paperino", 30, "MN889XZ", department1)
    department1.add_professor(professor2)

    try:
        professor2.assign_to_course(course_1)
    
    except ValueError as err:
        print("FAILURE:\n")
        print(f"{err}")

    print("-"*100)


    print("DEPARTMENT OVERVIEW\n")
    print(department1)
    print("-"*100)

    print("PROFESSOR_2 OVERVIEW\n")
    print(professor2)

    print("-"*100)
    print("Added: course_1 to department1 <- Failure expeted", "\n" + "-"*100)
    
    try:
        department1.add_course(course_1)
    
    except ValueError as err:
        print("FAILURE:\n")
        print(err)

    print("-"*100 + "\n", "Created: student 1/2/3", "\n" + "-"*100)
    student1: Student = Student("Pippo", 49, "AH10B")
    student2: Student = Student("Pluto", 40, "AH14A")
    student3: Student = Student("Clarabella", 39, "AM02D")

    print("STUDENTS OVERVIEW:\n")
    print("[1]")
    print(student1)
    print("[2]")
    print(student2)
    print("[3]")
    print(student3)

    print("-"*100 + "\n""Added: student 1/2/3 to course1", "\n" + "-"*100)
    course_1.add_student(student1)
    course_1.add_student(student2)
    course_1.add_student(student3)

    print("STUDENTS OVERVIEW\n")
    print("[1]")
    print(student1)
    print("[2]")
    print(student2)
    print("[3]")
    print(student3)

    print("-"*100)
    print("DEPARTMENT OVERVIEW\n")
    print(department1)

    print("-"*100)
    print("COURSE_1 OVERVIEW\n")
    print(course_1)