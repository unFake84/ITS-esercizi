import re
from re import Match

class FlightTime:
    check: str

    def __init__(self, check: str) -> None:
        pre_check: Match = re.fullmatch(r"^([0-9]{2}):([0-9]{2})$", check) # ore 00:00 min

        if pre_check is None:
            raise ValueError("Invalid time format: Expected 'hh:mm' with hours from 00 to 99 and minutes from 00 to 59.")

        hour: int = int(pre_check.group(1))
        minutes: int = int(pre_check.group(2))

        if hour < 0 or hour > 99:
            raise ValueError(f"Invalid Hour: Hour must be between 00 and 99. Provided: {hour:02}")
        if minutes < 0 or minutes > 59:
            raise ValueError(f"Invalid Minutes: Minutes must be between 00 and 59. Provided: {minutes:02}")

        self.check = f"{hour:02}h:{minutes:02}m"

    def __str__(self):
        return self.check