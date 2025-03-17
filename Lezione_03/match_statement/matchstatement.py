# insert a number
n:int = int(input("insert finishing position: "))

# check inserted number and return the position in cardinal form

# match statement
match n:

    # n=1
    case 1:
        
        print(f"{n}st!")

    # n=2
    case 2:

        print(f"{n}nd!")

    # n=3
    case 3:

        print(f"{n}rd!")

    # default case
    case _:

        print(f"{n}th!")