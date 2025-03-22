'''
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu
'''

# 1
class Food:

    def __init__(self, name: str, price: float, description: str):

        self.name = name
        self.price = price
        self.description = description

# 3.
class Menu:

    def __init__(self, lista: list[Food] = []):

        self.lista = lista

    # 4.
    def setaddFood(self, addfood: Food):

        self.lista.append(addfood)

    def getaddFood(self):

        return self.lista
    
    def setremoveFood(self, removefood: Food):

        if removefood in self.lista:

            self.lista.remove(removefood)

        else:

            print(f"{removefood.name.title()} non trovato nella lista")

    def getremoveFood(self):

        return self.lista
    
    # 6a.
    def printPrices(self):

        for i in self.lista:

            print(f"Nome: {i.name}\nPrezzo: {i.price} €")
            print("-------------------")

    # 7.
    def getAveragePrice(self):

        average = 0

        for i in self.lista:

            average += i.price

        return average / len(self.lista)

if __name__ == "__main__":

    # 2.
    burger: Food = Food("Chicken Royal", 10.90, "Chicken, tomato, cheese, bacon, salad")
    pizza: Food = Food("Margherita", 8, "Tomato, buffalo mozzarella, basilico")
    pasta: Food = Food("Carbonara", 12, "Eggs, pillow, parmesan cheese")

    # 3.
    lista: list[Food] = [burger, pizza, pasta]

    # 5.
    carne: Food = Food("Kobe Beef", 549.80, "Japanese beef")
    pesce: Food = Food("Spigola", 35, "Patate al forno, limone, sale")
    antipasto: Food = Food("Bruschetta", 5, "Pane, pomodoro, sale, aglio, olio")

    menu: Menu = Menu(lista) 

    menu.setaddFood(carne)
    menu.setaddFood(pesce)
    menu.setaddFood(antipasto)

    # 6b.
    menu.printPrices()
    media = menu.getAveragePrice()
    print(f"La media è {media:.2f}")