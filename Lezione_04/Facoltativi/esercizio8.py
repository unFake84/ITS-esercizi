'''
ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
    Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.

'''

from datetime import datetime

def account(
    id: int,
    name: str,
    last_name: str,
    fund: int|float
    ) -> tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]:

    operation: tuple[str, int|float, datetime] = ("Deposit", fund, datetime.now())
    # per formattare in stringa leggibile => var = datetime.now() \n var.strftime("%Y-%m-%d %H:%M:%S")

    t: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = (
    id,
    name,
    last_name,
    fund,
    [operation]
    )

    return t

def bank(
    database: list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]],
    account: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]
    ) -> list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]]:

    if database == []:
        database.append(account)

        return database

    else:
        flag: bool = False

        for acc in database:

            if acc[0] == account[0]:
                flag = True

        if not flag:
            database.append(account)

            return database

        else:
            raise ValueError("Account allready exists")

def atm(
    database: list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]],
    id: int,
    selection: str,
    amount: int = None
    ) -> None|str|list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]]:

    if selection == "balance":
        string_1: str = ""

        for t in database:

            if id == t[0]:
                string_1 = f"Account number:   {t[0]}\n"\
                            f"Account name:     {t[1]} {t[2]}\n"\
                            f"Current budget:   {t[3]:.2f}"

                print(string_1)

                return string_1

    elif selection == "deposit":
        if amount is not None and amount > 0:

            for i, acc in enumerate(database):

                if id == acc[0]:
                    operation: tuple[str, int|float, datetime] = ("Deposit", amount, datetime.now())
                    acc[4].append(operation)
                    new_sum: int|float = acc[3] + amount
                    repl_tuple: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = (
                        acc[0],
                        acc[1],
                        acc[2],
                        new_sum,
                        acc[4]
                    )
                    database[i] = repl_tuple

                    return database

            raise ValueError("Account not found")

        elif amount is None:
            raise ValueError("Amount required")

        else:
            raise ValueError("A positive amount is required for this transaction.")

    elif selection == "withdraw":
        if amount is not None and amount > 0:

            for i, a in enumerate(database):

                if id == a[0]:
                    check_fund: int|float = a[3] - amount

                    if check_fund < 0:
                        raise ValueError("This operation is not possible.")

                    operation: tuple[str, int|float, datetime] = ("Withdraw", amount, datetime.now())
                    a[4].append(operation)
                    repl_tuple: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = (
                        a[0],
                        a[1],
                        a[2],
                        check_fund,
                        a[4]
                    )
                    database[i] = repl_tuple

                    return database

            raise ValueError("Account not found.")

        elif amount is None:
            raise ValueError("Amount required")

        else:
            raise ValueError("A positive amount is required for this transaction.")

    else:
        raise ValueError("Selection not valid.")

if __name__ == "__main__":

    database: list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]] = []

    account_1: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = account(
        1,
        "Mario",
        "Rossi",
        20000
        )
    account_2: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = account(
        2,
        "Pino",
        "Pano",
        14000.15
        )
    account_3: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = account(
        3,
        "Uccio",
        "Uccia",
        44761
        )
    account_4: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = account(
        4,
        "Romualdo",
        "Latrinini",
        9700.86
    )
    account_5: tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]] = account(
        1,
        "Mario",                            # account di test
        "Rossi",
        30000
        )


    bank(database, account_1)
    bank(database, account_2)
    bank(database, account_3)
    bank(database, account_4)
    # bank(database, account_5)
    # bank(database, account_2)

    atm(database, 4, "deposit", 1700)
    atm(database, 1, "withdraw", 149.99)
    # atm(database, 1, "balance")

    print("-"*50)

    for n in database:

        print(f"{'Id':<4} {'Name':<10} {'Lastname':<10} {'Fund':<10}")
        print(f"{n[0]:<4} {n[1]:<10} {n[2]:<10} {n[3]:<10.2f}")
        print("\nStatement:")
        print(f"{'Date':<10} {'Time':<8} {'Amount':<10} {'Operation':<10}")

        for o in n[4]:

            print(f"{o[2].strftime('%Y-%m-%d %H:%M:%S'):<10} {o[1]:<10.2f} {o[0]:<10}")

        print("-"*50)