import re
from re import Match

class IATACode:
    check: str

    def __init__(self, check: str) -> None:        
        pre_check: Match = re.fullmatch(r"^[A-Z]{3}$", check) # <- es. FCO 

        if pre_check is None:
            raise ValueError("Invalid IATACode")

        self.check = pre_check.group(0)

    def __str__(self):
        return self.check
    
    def __eq__(self, other):
        if other is None or not isinstance(other, IATACode) or hash(self) != hash(other):
            return False
        return self.check == other.check
    
    def __hash__(self):
        return hash(self.check)