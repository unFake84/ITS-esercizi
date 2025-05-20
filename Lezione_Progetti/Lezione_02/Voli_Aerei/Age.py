import re
from re import Match

class Age:
    check: str

    def __init__(self, check) -> None:
        pre_check: Match = re.search(r"^19\d\d$|2[0-1]\d\d$")

        if pre_check is None:
            raise ValueError("Invalid date")
        
        self.check: str = pre_check.group(0)