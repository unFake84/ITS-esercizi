class Persona:

    def __init__(self, name: str, lastname: str, age: int):

        self.setname(name)
        self.setlastname(lastname)
        self.setage(age)

    def __str__(self) -> str:

        return f"\nName: {self.name}\nLastname: {self.lastname}\nAge: {self.age}"
    
    def __call__(self):

        if self.age < 18:

            print(f"{self.name} {self.lastname} is a minor!")

        elif self.age >= 18 and self.age < 30:

            print(f"{self.name} {self.lastname} is a young adult!")

        elif self.age >= 30 and self.age < 80:

            print(f"{self.name} {self.lastname} is an adult!")

        else:

            print(f"{self.name} {self.lastname} is a senior!")

    def setname(self, name: str):

        if name:
        
            self.name = name

        else:

            print("Error, name cannot be empty!")

    def getname(self):

        return self.name

    def setlastname(self, lastname: str) -> None:

        if lastname:

            self.lastname = lastname

        else:

            print("Error, lastname cannot be empty!")

    def getlastname(self):

        return self.lastname

    def setage(self, age: int) -> None:

        if age < 1 or age > 130:

            self.age = 0

        else:

            self.age = age

    def getage(self):

        return self.age

    def displaydata(self) -> None:

        print(f"\nName: {self.name}\nLastnmame: {self.lastname}\nAge: {self.age}\n")