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

class Department:

    def __init__(self, department_name: str) -> None:
        self.department_name = department_name
        self.courses = []
        self.professors = []

    def add_course(self, n_nourse: Course) -> None:
        if n_nourse not in self.courses:
            self.courses.append(n_nourse)
        
        else:
            raise ValueError("Not added, course already in the system")
    
    def add_professor(self, prof: Professor) -> None:
        if prof not in self.professors:
            self.professors.append(prof)
        
        else:
            raise ValueError(f"Professor {prof} is already present in this department")

    def __str__(self) -> str:
        courses_str: str = '\n '.join([c.course_name for c in self.courses]) if self.courses else 'No courses yet'
        profs_str: str = '\n' + f"\n{'-'*28}\n".join([str(p) for p in self.professors]) if self.professors else 'No associate professors'
        qnti_prof: int = len(self.professors) if self.professors else 0

        return f"Department name: {self.department_name}\n"\
                f"Courses: {courses_str}\n"\
                f"Professors: {qnti_prof}\n{profs_str}"

if __name__ == "__main__":

    department1: Department = Department("Dipartimento 1")

    print(department1)
    print("-"*50 + '\n')

    course_1: Course = Course("Math", "H001")
    professor1: Professor = Professor("Baudo", 60, "ZZ001AA", department1)

    department1.add_course(course_1)
    department1.add_professor(professor1)

    print(department1)
    print("-"*50 + '\n')

    professor2: Professor = Professor("Paperino", 30, "MN889XZ", department1)
    department1.add_professor(professor2)

    print(department1)
    print("-"*50 + '\n')