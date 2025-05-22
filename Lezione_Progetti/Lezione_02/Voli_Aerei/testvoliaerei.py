from voliaerei import *
from typing import Any
from FlightCode import FlightCode
from IATACode import IATACode
from Year import Year
from FlightTime import FlightTime

import unittest
from FlightCode import FlightCode
from IATACode import IATACode
from Year import Year
from FlightTime import FlightTime

print("\t", "-"*10, "[Volo Class]", "-"*10)

volocod: FlightCode = FlightCode("AA 1234")
volotime: FlightTime = FlightTime("01:24")
a1: Volo = Volo(volocod, volotime)
a2: Volo = Volo(volocod, volotime)

print("• a1:", a1, "\n", "• a2:", a2)
print("• a1 and a2 have same flightcode?:", a1 == a2)

diziodivoli: dict[FlightCode, FlightTime] = {
    a1: "First flight",
    a2: "Second flight"
}

print(f"• Flight collections without duplicates: {len(diziodivoli)}")
print("• a1 is same istance of a2?:", a1 is a2)

print("\t", "-"*10, "[Città + Nazione classes]", "-"*10)
nazione_italia: Nazione = Nazione("Italy")
citta1: Citta = Citta("Roma", 80000, nazione_italia)
citta2: Citta = Citta("Roma", 80000, nazione_italia)

print(f"• citta1: {citta1}")
print(f"• citta2: {citta2}")
print("• Q: citta1 is same istance of citta2?:", citta1 == citta2)

setcitta: set[Any] = {citta1, citta2}

print(f"• Set without duplicates: {len(setcitta)}")

print("\t", "-"*10, "[Aeroporto class]", "-"*10)

codporto1: IATACode = IATACode("FCO") # <- no univoco
codporto2: IATACode = IATACode("FCO")
codporto3: IATACode = IATACode("LIN")
portonome1: str = "DaVinci"
portonome2: str = "DaVinci"
portonome3: str = "Linate"
aeroporto1: Aeroporto = Aeroporto(codporto1, portonome1)
aeroporto2: Aeroporto = Aeroporto(codporto2, portonome2)
aeroporto3: Aeroporto = Aeroporto(codporto3, portonome3)

print(f"• airport1: {aeroporto1}")
print(f"• airport2: {aeroporto2}")
print(f"• airport3: {aeroporto3}")
print("• airport2 was not added because an identical airport[1] already existed:", aeroporto1 == aeroporto2)
## NOTA: il confronto tra aeroporti richiede sia il codice IATA che il nome
# perché esistono rari casi in cui lo stesso codice IATA è condiviso da più scali. (circa300)

dizioporti: dict[IATACode, str] = {
    codporto1: portonome1,
    codporto2: portonome2,
    codporto3: portonome3
}
print(f"• Collection of airports in an imaginary dictionary, length: {len(dizioporti)}")

print("\t", "-"*10, "Compagnia class", "-"*10)

companyNome1: str = "Dioni&Co"
companyYear1: Year = Year("1984")
company1: Compagnia = Compagnia(companyNome1, companyYear1)

print("• ", company1)

company2: Compagnia = Compagnia(companyNome1, companyYear1)
companyNome2: str = "Banana&Co"
companyYear2: Year = Year("2199")
company3: Compagnia = Compagnia(companyNome2, companyYear2)

print("• ", company3)

#UNITTEST v/TIPI DI DATO

print("\n\t---v--- UNITTEST ---v---\n")
print("FLIGHTCODE -> Regex not complied with AA 0A00")

class TestFlightCode(unittest.TestCase):

    def test_INIT(self):
        with self.assertRaises(ValueError):

            FlightCode("AA 0A00")

print("IATACODE -> Regex not complied with FC0")

class TestIATACode(unittest.TestCase):

    def test_INIT(self):
        with self.assertRaises(ValueError):

            IATACode("FC0")

print("YEAR -> Regex not complied with 1899")

class TestYear(unittest.TestCase):

    def test_INIT(self):
        with self.assertRaises(ValueError):

            Year("1899")

print("FLIGHTTIME -> Regex not complied with 02:60")

class TestFlightTime(unittest.TestCase):

    def test_INIT(self):
        with self.assertRaises(ValueError):

            FlightTime("02:60")

unittest.main()