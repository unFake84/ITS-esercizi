def recursivePower(a: int, b: int) -> int:

    if a < 0 or b < 0:

        print("Errore i numeri sono negativi")

    elif b == 0:

        return 1

    else:

        return a * recursivePower(a, b - 1)
    
print(recursivePower(3, 4))