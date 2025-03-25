'''
Three Restaurants:
Start with your class from Exercise 9-1.
Create three different instances from the class,
and call describe_restaurant() for each instance.
'''

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:

        print(
            f"Nome ristorante: {self.restaurant_name}\n" \
              f"Tipo di cucina: {self.cuisine_type}" \
                )
        
    def open_restaurant(self) -> None:

        print(f"Il ristorante {self.restaurant_name} è aperto!")

if __name__ == "__main__":

    restaurant: Restaurant = Restaurant("D&D da Dioni", "As long as the food is good!")

    print("-----------------------" * 2)
    print("Primo attributo:", restaurant.restaurant_name)
    print("Secondo attributo:", restaurant.cuisine_type)
    print("-----------------------" * 2)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # ex9_2.
    restaurant_2: Restaurant = Restaurant("Da Python", "Let's chew on some code")
    restaurant_3: Restaurant = Restaurant("Ucc's Jazz", "Jazz and Food")
    restaurant_4: Restaurant = Restaurant("1870","Belle cuisine")

    print("-----------------------" * 2)
    restaurant_2.describe_restaurant()
    print("-----------------------" * 2)
    restaurant_3.describe_restaurant()
    print("-----------------------" * 2)
    restaurant_4.describe_restaurant()
    print("-----------------------" * 2)