'''
Login Attempts:

1.
    Add an attribute called login_attempts to your User class from Exercise 9-3.

2.
    Write a method called increment_login_attempts()
    that increments the value of login_attempts by 1.

3.   
    Write another method called reset_login_attempts()
    that resets the value of login_attempts to 0.
  
4.
    Make an instance of the User class and call increment_login_attempts() several times.

5.
    Print the value of login_attempts to make sure it was incremented properly,
    and then call reset_login_attempts().

6.
    Print login_attempts again to make sure it was reset to 0.
    
'''

# ex 9_3.
class User:

    # 1aI.
    def __init__(self, first_name: str, last_name: str, age: int, country: str, city: str, address: str, cap: int, login_attempts: int = 0):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.address = address
        self.cap = cap

        # 1aII.
        self.login_attempts = login_attempts

    def describe_user(self) -> None:

        profilo = (            
            f"Nome: {self.first_name}\n"
            f"Cognome: {self.last_name}\n"
            f"Età: {self.age}\n"
            f"Nazione: {self.country}\n"
            f"Città: {self.city}\n"
            f"Indirizzo: {self.address}\n"
            f"Cap: {self.cap}\n"
            )
        
        print(profilo)
    
    def greet_user(self) -> None:

        print("Benvenuto", self.first_name + "!")
        print("-" * 30)

    # 2.
    def increment_login_attempts(self):

        self.login_attempts += 1

    # 3.
    def reset_login_attempts(self):

        self.login_attempts = 0

if __name__ == "__main__":

    print("-" * 30)
    print("Inizializzazione utenti.")
    print("-" * 30)
    
    user1: User = User("Pippo", "Pappo", 93, "Piponia", "Piptown", "Viale Papese -4", 9999)
    user2: User = User("Bob", "boB", 340,"B.o.b. states", "Boma", "Via dei bobbi 0", 1111111111)
    user3: User = User("Giovanni", "Verdi", 40, "Italia", "Torino", "Corso Francia 8", 10100)
    user4: User = User("Franz", "Liszt", 74, "Ungheria", "Budapest", "Residenza in Europa", 1011)
    user5: User = User("Napoleone", "Bonaparte", 156, "Francia", "Ajaccio", "Palazzo imperiale", 20000)

    user1.describe_user()
    user1.greet_user()

    user2.describe_user()
    user2.greet_user()

    user3.describe_user()
    user3.greet_user()

    user4.describe_user()
    user4.greet_user()

    user5.describe_user()
    user5.greet_user()

    # 4.
    user1.increment_login_attempts()
    user2.increment_login_attempts()
    user3.increment_login_attempts()
    user4.increment_login_attempts()
    user5.increment_login_attempts()

    # 5a.
    print("-" * 45)
    print(f"L'utente '{user1.last_name}', ha effettutato: {user1.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user2.last_name}', ha effettutato: {user2.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user3.last_name}', ha effettutato: {user3.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user4.last_name}', ha effettutato: {user4.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user5.last_name}', ha effettutato: {user5.login_attempts} login.")
    print("-" * 45)

    # 5b.
    user1.reset_login_attempts()
    user2.reset_login_attempts()
    user3.reset_login_attempts()
    user4.reset_login_attempts()
    user5.reset_login_attempts()

    # 6.
    print("-" * 45)
    print(f"L'utente '{user1.last_name}', ha effettutato: {user1.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user2.last_name}', ha effettutato: {user2.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user3.last_name}', ha effettutato: {user3.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user4.last_name}', ha effettutato: {user4.login_attempts} login.")
    print("-" * 45)
    print(f"L'utente '{user5.last_name}', ha effettutato: {user5.login_attempts} login.")
    print("-" * 45)