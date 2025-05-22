import re
from re import Match

class FlightCode:
    check: str # <- inizializzo una variabile condivisa tra tutti i metodi della classe FlightCode

    def __init__(self, check: str) -> None:
        pre_check: Match = re.fullmatch(r"^[A-Z]{2} \d{4}$", check) # regex = es. AA 1234
        if pre_check is None:
            raise ValueError("Invalid FlightCode")

        self.check = pre_check.group(0) # <- group(0) prende tutta la stringa da pre_check

    def __str__(self) -> str:
        return self.check

    def __eq__(self, other: "FlightCode") -> bool:

        # se l' altro oggetto è None oppure non è istanza di FlightCode oppure "questo hash" è divero dall'"altro hash"
        if other is None or not isinstance(other, FlightCode) or hash(self) != hash(other):
            return False # <- cioè, i due oggetti non sono uguali
        return self.check == other.check

    # consente di poter creare set o dizionari (immutabili)
    def __hash__(self) -> int:
        return hash(self.check)