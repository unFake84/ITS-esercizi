'''
Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.

        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.

            get_balance(): restituisce il saldo corrente del conto.

    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.

        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            Solleva il seguente KeyError "Account with this ID already exists" se l'account con l'ID specificato esiste già.

            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.

            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
            Solleva il seguente  KeyError "Account not found" se l'account non esiste.
'''

class Account:

    def __init__(self, account_id: str):
        self.account_id: str = account_id
        self.balance: float = 0

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def get_balance(self) -> float:
        return self.balance

class Bank:

    def __init__(self, accounts: dict[str, Account] = None) -> None:
        self.accounts: dict[str, Account] = accounts if accounts is not None else {}

    def create_account(self, account_id: str) -> None:
        if account_id not in self.accounts:

            self.accounts[account_id] = Account(account_id)

        else:
            raise KeyError("Account with this ID already exists")

    def deposit(self, account_id: str, amount: float) -> None:
        if account_id in self.accounts:

            self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str) -> float:
        if account_id in self.accounts:

            return self.accounts[account_id].get_balance()

        else:
            raise KeyError("Account not found")