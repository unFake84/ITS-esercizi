'''
Imported Admin:

1.
    Create a module users.py containing three classes:

    1a.
        User: stores first_name, last_name, username, and email;
        includes describe_user() and greet_user() methods.

    1b.
        Privileges: holds a list of privileges and a method show_privileges() to display them.

    1c.
        Admin: stores a User instance and a Privileges instance as attributes.
        
2.
    In a separate file main.py, import the classes,
    create a User and a Privileges instance, pass them to Admin,
    and call describe_user() and show_privileges() to verify everything works correctly.

'''

# 1a.
class User:

    def __init__(self, first_name: str = "inserire nome", last_name: str = "inserire cognome", username: str = "inserire username", email: str = "inserire email"):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username.lower()
        self.email = email

    def describe_user(self) -> str:

        profilo = (
            f"\tNome: {self.first_name.title()}\n"
            f"\tCognome: {self.last_name.title()}\n"
            f"\tUsername: {self.username.capitalize()}\n"
            f"\tEmail:  {self.email}\n"
        )

        return f"Dettagli Utente:\n{profilo}"

    def greet_user(self) -> None:

        print(f"Benvenuto {self.username.capitalize()}!")
        print("_" * 30)

# 1b.
class Privileges:

    def __init__(self, lista: list[str] = ["amministratore", "utente", "visitatore"]):

        self.lista = lista

    def show_privileges(self) -> list:

        indice = 1
        ruolo = []

        for privilegio in self.lista:

            # print(f"\t{indice}: {privilegio}")
            indice += 1
            ruolo.append(privilegio)
        
        print("Ruolo Utente:", "\t\n", *ruolo, sep= "")

# 1c.
class Admin:

    def __init__(self, user: User = User(), privilegi: Privileges = Privileges()):

        self.user = user
        self.privilegi = privilegi


# "Pinco", "Panco", "PancoPinco", "PeP@punco.poc"