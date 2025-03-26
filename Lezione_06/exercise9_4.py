'''
Number Served:

1.
    Start with your program from Exercise 9-1.
    Add an attribute called number_served with a default value of 0.

2.
    Create an instance called restaurant from this class.
    Print the number of customers the restaurant has served,
    and then change this value and print it again.

3.
    Add a method called set_number_served() that lets you
    set the number of customers that have been served.
    Call this method with a new number and print the value again.

4.
    Add a method called increment_number_served()
    that lets you increment the number of customers who’ve been served.
    Call this method with any number you like that could represent
    how many customers were served in, say, a day of business.

'''

class Restaurant: 

    # 1a.    
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served = 0):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 1b.
        self.number_served = number_served
        # # 4b.
        # self.costumer_served + number_served

    def describe_restaurant(self) -> None:

        print(
            f"Nome ristorante: {self.restaurant_name}\n" \
              f"Tipo di cucina: {self.cuisine_type}" \
                )
        
    def open_restaurant(self) -> None:

        print(f"Il ristorante '{self.restaurant_name}' è aperto!")

    # 3a.
    def set_number_served(self, number_served = 0) -> None:

        self.number_served = number_served

    def get_number_served(self):

        return self.number_served
    
    # 4a.
    def increment_number_served(self, increment = 0):

        self.number_served += increment

if __name__ == "__main__":

    # 2a.
    restaurant: Restaurant = Restaurant("D&D da Dioni", "Basta che il cibo sia buono!", 50)
    

    print("Primo attributo:", restaurant.restaurant_name)
    print("Secondo attributo:", restaurant.cuisine_type)
    print("-----------------------" * 2)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # 2b.
    print("Ha appena servito", restaurant.number_served, "clienti.")
    print("-----------------------" * 2)

    # 3b.
    restaurant.set_number_served(20)
    print("Il nuovo valore dell' attributo 'number_served' è :", restaurant.get_number_served())

    # 4a.
    increment_value: int = 35
    restaurant.increment_number_served(increment_value)
    print("Sono stati aggiunti altri", increment_value, "clienti.")

    # 4c.
    print("Oggi sono stati serviti", restaurant.get_number_served(), "clienti.")