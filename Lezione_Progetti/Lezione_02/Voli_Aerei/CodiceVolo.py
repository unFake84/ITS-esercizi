import re
from re import Match

class CodiceVolo:
    check: str
    
    def __eq__(self, other: "CodiceVolo") -> bool:
        if other is None or not isinstance(other, CodiceVolo) or hash(self) != hash(other):
            return False
        return self.check == other.check

    def __hash__(self) -> int:        
        return hash(self.check)

    def __str__(self) -> str:
        return self.check

    def __init__(self, check) -> None:
        pre_check: Match = re.search(r"^[A-Z]{2} \d{4}$", check)
        if pre_check is None:
            raise ValueError("Invalid Code")

        self.check: str = pre_check.group(0)