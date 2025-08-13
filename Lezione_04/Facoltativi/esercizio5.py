'''
Inventory Management System:

    Create a list to store the items in inventory.
    Create a function that defines an item with a code, name, quantity, and price.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops to manage the various inventory operations.

'''

def item(code: int, name: str, quantity: int, price: float) -> dict[int, dict[str, str | int | float]]:
    d: dict[int, dict[str, str | int | float]] = {
        code: {
            "name": name,
            "quantity": quantity, 
            "price": price
        }
    }

    return d

if __name__ == "__main__":

    inventory: list[dict[int, dict[str, str | int | float]]] = [] # RIPRENDERE QUI, VEDERE SE LISTA O DIZIONARIO

    i1: dict[int, dict[str, str | int | float]] = item(100, "Mouse", 1, 25 )
    inventory.append(i1)
    print(inventory)