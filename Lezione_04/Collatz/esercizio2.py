def ifprimo(n: int) -> bool:

    primo = True

    if n < 2:

        print("Il numero è primo")
        return True

    else:

        div = 2

        while div < n:

            if n % div == 0:

                print("il numero non è primo")
                primo = False
                return False

            div += 1

        if primo:
            
            print("Il numero è primo")
            return 
        
numeri: list[int] = ifprimo(11)