'''
ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
    Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.

'''

def account(id: int, name: str, last_name: str, fund: int|float) -> tuple[int, str, str, int|float]:

    t: tuple[int, str, str, int|float] = (id, name, last_name, fund)
    return t

def bank():
    pass

def atm() -> float:
    pass

if __name__ == "__main__":

    account_1: tuple[int, str, str, int|float] = account(1, "Mario", "Rossi", 20000)
    account_2: tuple[int, str, str, int|float] = account(2, "Pino", "Pano", 14000.15)
    account_3: tuple[int, str, str, int|float] = account(3, "Uccio", "Uccia", 44761)
    account_4: tuple[int, str, str, int|float] = account(4, "Romualdo", "Latrinini", 9700.86)
    print(account_1)