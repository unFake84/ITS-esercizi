import re
from re import Match

class IATACode:
    check: str

    def __str__(self) -> str:        
        return self.check

    def __init__(self, check) -> None:        
        pre_check: Match = re.search(r"^[A-Z]{3}$", check)

        if pre_check is None:
            raise ValueError("Invalid Code")
        
        self.check: str = pre_check.group(0)