from typing import Self
from datetime import datetime
import re

class RealGEZ(float):

	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: float = float.__new__(cls, v)

		if n >= 0:

			return n

		raise ValueError(f"The value {n} is negative!")

class CAP(str):

	def __new__(cls, cap: str) -> Self:
		if re.fullmatch(r'^\d{5}$', cap):

			return super().__new__(cls, cap)
		
		raise ValueError(f"The string “{cap}” is not a valid Italian postcode!")
     
class Indirizzo:

    _via: str
    _cap: CAP

    def __init__(self, via: str, cap: CAP) -> None:

        self._via = via
        self._cap = cap

    def __str__(self):

        return (
            f"Address: {self._via}\n"
            f"Cap: {self._cap}\n"
            )
	
class Date:

    def __init__(self, date: str):
        try:

            self.date = datetime.strptime(date, "%d.%m.%Y").date()

        except ValueError:
            raise ValueError("Date not valid")

    def __eq__(self, other: "Date"):

        return self.date == other.date

    def __str__(self):
        convert_to_str: str = self.date.strftime("%d.%m.%Y")

        return convert_to_str