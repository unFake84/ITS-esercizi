'''
Users:

1.
    Make a class called User.
    Create two attributes called first_name and last_name,
    and then create several other attributes
    that are typically stored in a user profile.

2.
    Make a method called describe_user() that prints
    a summary of the user’s information.
    Make another method called greet_user()
    that prints a personalized greeting to the user.

3.
    Create several instances representing different users,
    and call both methods for each user.

'''
# 1.
class User:

    def __init__(self, first_name: str, last_name: str, age: int, country: str, city: str, address: str, cap: int):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.address = address
        self.cap = cap

    # 2.
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

if __name__ == "__main__":

    print("-" * 30)
    print("Inizializzazione utenti.")
    print("-" * 30)
    
    # 3.
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