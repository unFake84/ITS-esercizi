'''
    [7]
    Finally, write a simple driver program.
    After creating a University, you should begin by creating instances of the main components that
    make up a university:

        Departments (e.g., Computer Science, Literature)

        Courses (e.g., Data Structures, Medieval Literature)

        Professors (e.g., faculty members who will teach the courses)

        Students (e.g., individuals who will enroll in the courses)

    Once these instances are created, follow these steps:

        Add all entities to the university: Ensure the university class can register departments and students. 

        Enroll students in courses: Simulate student registration by assigning students to one or more courses. 

        Assign professors to courses: Each course should have a professor responsible for teaching it. 

        Display the state of the university:
        at each significant step, print out a summary of the university’s current state. This might include:
            A list of courses with assigned professors.
            Which students are enrolled in which courses.
            A breakdown of departments and the courses they offer.

'''

from person import Person
from student import Student
from professor import Professor
from course import Course
from department import Department
from university import University
import random

#DEPARTMENTS
department1: Department = Department("Computer Science")
department2: Department = Department("Literature")

# COURSES
course1: Course = Course("Data Structures", "0001")
course2: Course = Course("Medieval Literature", "0002")

# PROFESSORS
professor1: Professor = Professor("Corrado Corradini", 58, "100")
professor2: Professor = Professor("Marco De Angelis", 60, "101")

# STUDENTS
student1: Student = Student("Pippo", 49, "AH10B")
student2: Student = Student("Pluto", 40, "AH14A")
student3: Student = Student("Clarabella", 39, "AM02D")
student4: Student = Student("Paperoga", 31, "AI01F")
student5: Student = Student("Topolina", 28, "AF08A")
student6: Student = Student("Paperino", 30, "MN89Z")
student7: Student = Student("Gastone", 29, "AA000A")
student8: Student = Student("Paperina", 27, "AF09A")
student9: Student = Student("Topolino", 31, "GH01C")

# UNIVERSITY
university1: University = University("Paperopoli & Topolinia University")

university1.add_department(department1)
university1.add_department(department2)

university1.add_student(student1)
university1.add_student(student2)
university1.add_student(student3)
university1.add_student(student4)
university1.add_student(student5)
university1.add_student(student6)
university1.add_student(student7)
university1.add_student(student8)
university1.add_student(student9)

# COURSES >>> DEPARTMENT
department1.add_course(course1)
department2.add_course(course2)

# STUDENT >>> COURSES
list_of_students: list[Student] = [
    student1,
    student2,
    student3,
    student4,
    student5,
    student6,
    student7,
    student8,
    student9
]

# MODO CASUALE, PUO AVERE RIPETIZIONI CASUALI
# for i, student in enumerate(list_of_students, 1):

#     try:

#         if i <= 3:
#             course1.add_student(random.choice(list_of_students))

#         elif i > 3 and i <= 6:
#             course2.add_student(random.choice(list_of_students))

#         # i restanti 3 sicuramente non sono iscritti a nessun corso

#     except ValueError as err:
#         print(f"{err} <- No course assigned")

# PRENDE TUTTI GLI STUDENTI ED OGNUNO HA 3 POSSIBILITÀ (corso1, corso2, nessun corso)
for student in list_of_students:

    scelta: int = random.randint(1, 3)

    if scelta == 1:
        course1.add_student(student)

    elif scelta == 2:
        course2.add_student(student)

print("#"*130)

# PROFESSORS >>> COURSES >>> DEPARTMENT
course1.set_professor(professor1)
professor2.assign_to_course(course2)

professor1.set_department(department1)
# professor2.set_department(department2)        # entrambi possono assegnarsi ad un dipartimento
# department1.add_professor(professor1)         # entrambi possono assegnarsi ad un dipartimento
department2.add_professor(professor2)

print(university1)
print("#"*130)