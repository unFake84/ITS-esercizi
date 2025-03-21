'''
1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.
'''

class Student:

    def __init__(self, name: str, studyProgram: str, age: int, gender: str):

        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self) -> None:

        #print(f"At the {self.name} of my perspective is the course {self.studyProgram}")
        print(f"The student {self.name}, gender {self.gender} aged {self.age} is attending the course: {self.studyProgram}")

if __name__ == "__main__":
    
    center: Student = Student("Center", "FullStack", 40, "M")
    left: Student = Student("Left", "VideoMaker", 27, "M")
    right: Student = Student("Right", "CyberSec", 19, "F")

    center.printInfo()
    left.printInfo()
    right.printInfo()