'''
E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create functions that manage the shopping cart, allowing the user to
    add, remove, and view products in the cart.
    Create a function that calculates the cart total and apply any discounts or taxes.
    Create a funciton to print a detailed summary of the cart including products and totals.
    Implement a for loop to iterate over the items in the cart and print detailed information about
    each product and the total.

'''

def product(name: str, price: float, quantity: int) -> dict[str, list[float|int]]:

    d: dict[str, list[float|int ]] = {
        name:
        [
            price,
            quantity
        ]
    }

    return d

def addCart(cart: dict[str, list[float|int]], name: str, price: float, quantity: int) -> None:

    if name not in cart:
        cart[name] = [price, quantity]

    elif cart[name][0] == price:
        cart[name][1] += quantity

    else:
        print("Please note: prices do not match.")

def removeCart(cart: dict[str, list[float|int]], name: str, quantity: int = None) -> None:

    if name in cart and quantity is None:
        cart.pop(name)
        print(f"The product {name}, has been removed.")

    elif name in cart and quantity is not None:
        cart[name][1] -= quantity
        print(f"{quantity} items have been removed from {name}.")

        if cart[name][1] <= 0:
            cart.pop(name)
            print(f"The product {name}, has been removed.")

    else:
        print(f"Please note: the product {name}, is not in your cart.")

def viewCart(cart: dict[str, list[float|int]]) -> str:

    string: str = ""

    for item, product in enumerate(cart,1):
        string += f"{item} - {product}\n"

    return f"Cart contents:\n" + string

def discount(cart: dict[str, list[float|int]], discount: int) -> float|None:

    if discount >= 0 and discount <= 100:

        total: float = 0

        for price in cart.items():
            total += price[1][0] * price[1][1]

        disc: float = total / 100 * discount

        return round(total - disc, 2)

    else:
        print("Not valid, discount not applied, reapply discount")
        return None

def detailedSummary(cart: dict[str, list[float|int]]) -> str:

    string: str = ""
    total: float = 0

    for name in cart:

        string += f"\nName product: {name}\n"\
                    f"Price: {cart[name][0]}\n"\
                    f"Quantity: {str(cart[name][1])}\n"\
                    f"Total: {cart[name][0] * cart[name][1]:.2f}\n{'-' * 50}"

        total += cart[name][0] * cart[name][1]

    return f"Summary:" + string + "\n" + f"Total price of products: {total:.2f}\n{'-' * 50}"

if __name__ == "__main__":

    cart: dict[str, list[float|int]] = {}

    p1: dict[str, list[float|int]] = product("banana", 0.49, 3)
    # print( p1 )

    # tentativo manuale di estrapolare informazioni da p1 
    name_p1: str = "banana"
    price_p1: float = p1["banana"][0]
    quantity_p1: int = p1["banana"][1]

    # uso funzione addCart() per aggiungere il carrello
    addCart(cart, name_p1, price_p1, quantity_p1)
    addCart(cart, name_p1, price_p1, quantity_p1)
    addCart(cart, "fragola", 4.99, 1)
    addCart(cart, "lampone", 3.49, 3)

    # uso removeCart() per rimuovere un prodotto non esistente nel carrello (cart)
    removeCart(cart, "mela", 6)
    # per rimuovere qualche banana dal carrello (cart)
    removeCart(cart, "banana", 4)
    #print( cart )

    # elenco semplice del carrello
    print(viewCart(cart))

    # elenco dettagliato del carrello + ciclo for con totale
    print(detailedSummary(cart))

    # applico sconto
    sale1: float = discount(cart, 22)
    print(f"Discount applied correctly: {sale1}" if sale1 is not None else"Discount not applied")