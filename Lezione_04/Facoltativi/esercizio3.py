'''
Create a function that defines a product with a name, price, and quantity.
Create functions that manage the shopping cart, allowing the user to
add, remove, and view products in the cart.
Create a function that calculates the cart total and apply any discounts or taxes.
Create a funciton to print a detailed summary of the cart including products and totals.
Implement a for loop to iterate over the items in the cart and print detailed information about
each product and the total.
'''

def product( name:str, price:float, quantity:int ) -> dict[ str, list[ float | int ] ]:

    d: dict[ str, list[ float | int ] ] = {
        name:
        [
            price,
            quantity
        ]
    }

    return d

def addCart( cart:dict[ str, list[ float | int ] ], name:str, price:float, quantity:int ) -> None:

    if name not in cart:
        cart[ name ] = [ price, quantity ]

    elif cart[ name ][ 0 ] == price:
        cart[ name ][ 1 ] += quantity

    else:
        print( "Please note: prices do not match." )

def removeCart( cart:dict[ str, list[ float | int ] ], name:str, quantity: int = None ) -> None:

    if name in cart and quantity is None:
        cart.pop( name )

    elif name in cart and quantity is not None:
        cart[ name ][ 1 ] -= quantity

        if cart[ name ][ 1 ] <= 0:
            cart.pop( name )
            print( f"The product { name }, has been removed." )

    else:
        print( f"Please note: the product { name }, is not in your cart." )

def viewCart( view:str ) -> str:
    pass

if __name__ == "__main__":

    cart: dict[ str, list[ float | int ] ] = {}

    p1: dict[ str, list[ float | int ] ] = product( "banana", 0.49, 3 )
    print( p1 )
    
    # tentativo manuale di estrapolare informazioni da p1 
    name_p1: str = "banana"
    price_p1: float = p1[ "banana" ][ 0 ]
    quantity_p1: int = p1[ "banana" ][ 1 ]

    # uso funzione addCart() per aggiungere il carrello
    addCart( cart, name_p1, price_p1, quantity_p1 )
    addCart( cart, name_p1, price_p1, quantity_p1 )
    addCart( cart, "fragola", 4.99, 1 )

    # uso removeCart() per rimuovere un prodotto non esistente nel carrello (cart)
    removeCart( cart, "mela", 6 )
    print( cart )
