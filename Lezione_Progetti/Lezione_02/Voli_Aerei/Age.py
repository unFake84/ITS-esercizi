import re
from re import Match

class Age:
    check: str

    def __init__(self, check: str) -> None:
        pre_check: Match = re.fullmatch(r"^19\d\d$|2[0-1]\d\d$", check)

        if pre_check is None:
            raise ValueError("Invalid foundation date")
        
        self.check = pre_check.group(0)

    def __str__(self):
        return self.check