import re
from re import Match

class FlightCode:
    check: str
    
    def __eq__(self, other: "FlightCode") -> bool:
        if other is None or not isinstance(other, FlightCode) or hash(self) != hash(other):
            return False
        return self.check == other.check

    def __hash__(self) -> int:        
        return hash(self.check)

    def __init__(self, check: str) -> None:
        pre_check: Match = re.fullmatch(r"^[A-Z]{2} \d{4}$", check)
        if pre_check is None:
            raise ValueError("Invalid Code")

        self.check = pre_check.group(0)

    def __str__(self) -> str:
        return self.check