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
    ) -> None|list[tuple[int, str, str, int|float, list[tuple[str, int|float, datetime]]]]:

    if selection == "balance":
        string_1: str = ""
        for t in database:
            if id == t[0]:
                string_1 = f"Account number:   {t[0]}\n"\
                            f"Account name:     {t[1]} {t[2]}\n"\
                            f"Current budget:   {t[3]:.2f}"
                print(string_1)

    elif selection == "deposit":
        pass

    elif selection == "withdraw":
        pass

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
        "Mario",
        "Rossi",
        30000
        )

    
    bank(database, account_1)
    bank(database, account_2)
    bank(database, account_3)
    bank(database, account_4)
    # bank(database, account_5)
    # bank(database, account_2)

    atm(database, 1, "balance")



    # for n in database:
    #     print(n)






# for i, a in enumerate(database):
#     if a[0] == account[0]:
#         sum_ab: int|float = a[3] + account[3]
#         temp_tuple: tuple[int, str, str, int|float] = (account[0], account[1], account[2], sum_ab)
#         database[i] = temp_tuple