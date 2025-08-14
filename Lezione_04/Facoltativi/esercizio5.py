'''
Inventory Management System:

    Create a list to store the items in inventory.
    Create a function that defines an item with a code, name, quantity, and price.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops to manage the various inventory operations.

'''

def item(code: int, name: str, quantity: int, price: float) -> dict[int, dict[str,str|int|float]]:
    d: dict[int, dict[str, str | int | float]] = {
        code: {
            "name": name,
            "quantity": quantity, 
            "price": price
        }
    }

    return d

def addItem(
        inventory: list[dict[int, dict[str, str|int|float]]],
        item: dict[int, dict[str, str|int|float]]
    ) -> list[dict[int, dict[str, str|int|float]]]:

    id: int = list(item.keys())[0]      # va bene se la chiave è una sola

    if not inventory:
        inventory.append(item)
        print(f"Key: {id}, successfully added to inventory.")
        return inventory

    else:
        for ind, _ in enumerate(inventory):

            if id in inventory[ind]:
                inventory[ind][id]["quantity"] += item[id]["quantity"]
                # inventory[ind][id]["price"] *= item[id]["quantity"]       # prezzo non unitario
                print(f"Key: {id}, successfully added to {inventory[ind][id]['name']}'s item.")
                return inventory

        else:
            inventory.append(item)
            print(f"Key: {id}, successfully added to inventory.")
            return inventory

def delItem(
        inventory: list[dict[int, dict[str, str|int|float]]],
        id: int,
        quantity: int = None
    ) -> list[dict[int, dict[str, str|int|float]]]:

    if quantity is not None:
        for i, item in enumerate(inventory):

            if id in item:
                inventory[i][id]["quantity"] -= quantity

                if inventory[i][id]["quantity"] <= 0:
                    inventory.remove(item)
                    print(f"Key: {id}, successfully removed to inventory.")

                    return inventory

        print(f"Key: {id}, not found")
        return inventory

    elif quantity is None:
        for item in inventory:

            if id in item:
                inventory.remove(item)
                print(f"Key: {id}, successfully removed to inventory.")
                return inventory

        print(f"Key: {id}, not found")
        return inventory

def searchItem(inventory: list[dict[int, dict[str, str|int|float]]], id: int) -> str:

    founded: bool = False

    for i in inventory:

        if id in i:
            name: str = i[id]["name"]
            quantity: int = i[id]["quantity"]
            price: int|float = i[id]["price"]
            founded = True
            break

    if not founded:
        return f"Key: {id}, not found."

    overView: str = f"Key: {id}, founded - overview:\n"\
                    f"{'Name':<10} {'Quantity':<10} {'price/unit':<10}\n"\
                    f"{name:<10} {quantity:<10} {price:<10}\n"\
                    f"Total price: {price*quantity}"

    return overView

if __name__ == "__main__":

    inventory: list[dict[int, dict[str, str|int|float]]] = []

    # aggiungo manualmente 2 item nell'inventario che
    # in questo esercizio è rappresentato da una lista che
    # contiente items sotto forma di dizionario dove
    # la chiave è rappresentato dall'id del prodotto
    i1: dict[int, dict[str, str|int|float]] = item(100, "Mouse", 1, 25)
    i2: dict[int, dict[str, str|int|float]] = item(101, "Keyboard", 1, 35)
    # inventory.append(i1)
    # inventory.append(i2)

    i3: dict[int, dict[str, str|int|float]] = item(102, "Printer", 1, 90)
    addItem(inventory, i1)
    addItem(inventory, i1)
    addItem(inventory, i2)
    addItem(inventory, i3)
    addItem(inventory, i2)

    delItem(inventory, 100, 5)

    print(searchItem(inventory, 101))



    print("INVENTORY RAW VIEW")
    print(inventory)