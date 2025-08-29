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
        # dep_str: str = '\n'.join([str(d.department_name) for d in self.departments]) if self.departments else f"No departments in this university"
        # std_str: str = '\n'.join([str(s.name) for s in self.students]) if self.students else f"No students registered"

        #return f"University: {self.name}\n\n\nDepartments:\n{dep_str}\n\nStudents:\n{std_str}"
        final_string: str = f"\t\t\tUniversity: {self.name}\n\n"
        if not self.departments:
            final_string += "No departments in this university"
        
        else:
            final_string += "\nDepartments:\n\n"
            for dptm in self.departments:
                final_string += str(dptm) + "\n\n"
                if not dptm.courses:
                    final_string += "\n\nCONTINUARE CODICE\n\n" #AGGIUNGERE UN CORSO A DIPARTIMENTO1 PER VEDERE SE ENTRA NEL CICLO
        
        if not self.students:
            final_string += "\n\nNo students registered"
        
        return final_string


if __name__ == "__main__":

    university1: University = University("Uni1")

    print(university1)
    print("-"*150)

    department1: Department = Department("Dipartimento1")
    department2: Department = Department("Dipartimento2")
    department3: Department = Department("Dipartimento3")
    university1.add_department(department1)
    university1.add_department(department2)
    university1.add_department(department3)

    print(university1)
    print("-"*150)

    # try:
    #     university1.add_department(department1)

    # except ValueError as err:
    #     print(err)

    # print(university1)

    # student1: Student = Student("Pippo", 49, "AH10B")
    # student2: Student = Student("Pluto", 40, "AH14A")
    # student3: Student = Student("Clarabella", 39, "AM02D")

    # print("-"*150)
    # print(university1)

    # university1.add_student(student1)
    # university1.add_student(student2)
    # university1.add_student(student3)

    # print(university1)

    # try:
    #     university1.add_student(student1)

    # except ValueError as err:

    #     print(err)
    
    # print(university1)