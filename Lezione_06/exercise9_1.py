'''
Restaurant:

1.
    Make a class called Restaurant.
    The __init__() method for Restaurant should store
    two attributes: a restaurant_name and a cuisine_type.

2.
    Make a method called describe_restaurant()
    that prints these two pieces of information,
    and a method called open_restaurant() that
    prints a message indicating that the restaurant is open.

3.
    Make an instance called restaurant from your class.
    Print the two attributes individually, and then call both methods.
    
'''

# 1.
class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 2.
    def describe_restaurant(self) -> None:

        print(
            f"Nome ristorante: {self.restaurant_name}\n" \
              f"Tipo di cucina: {self.cuisine_type}" \
                )
        
    def open_restaurant(self) -> None:

        print(f"Il ristorante '{self.restaurant_name}' è aperto!")

if __name__ == "__main__":

    # 3.
    restaurant: Restaurant = Restaurant("D&D da Dioni", "As long as the food is good!")

    print("Primo attributo:", restaurant.restaurant_name)
    print("Secondo attributo:", restaurant.cuisine_type)
    print("-----------------------" * 2)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()