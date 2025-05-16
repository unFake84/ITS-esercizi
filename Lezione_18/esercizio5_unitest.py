import unittest
from esercizio5 import sum_OR_sub, FormulaError

# # Definiamo la classe di test per la funzione sum_OR_sub
class TestSumOrSub(unittest.TestCase):

    # I metodi devono iniziare con test se non, unittest ignora tali metodi
    # utilizzo assert.Equal per verificare i risultati corretti
    # utilizzo assert.Raises per verificare se vengono chiamate correttamente le eccezioni
    # utillo with insieme ad assert.Raises per confermare che l'errore sia previsto

    # controllo l'addizione
    def test_addition(self):

        self.assertEqual(sum_OR_sub("3 + 2"), 5.0)

    # sottrazione
    def test_subtraction(self):

        self.assertEqual(sum_OR_sub("10 - 7"), 3.0)

    # risultato negativo
    def test_negativeResult(self):

        self.assertEqual(sum_OR_sub("1 - 2"), -1.0)

    # se l'operatore non è [+] oppure [-]
    def test_invalidOperator(self):

        with self.assertRaises(FormulaError):
            
            sum_OR_sub("1 & 2")

    # se manca un numero
    def test_missingNumber(self):

        with self.assertRaises(FormulaError):

            sum_OR_sub("1 +")

    # controlla gli spazi
    def test_spaces(self):

        with self.assertRaises(FormulaError):

            sum_OR_sub("1 +     1")
    
    # testa se sono presenti numeri alfanumerici
    def test_wrongnumber(self):

        with self.assertRaises(FormulaError):

            sum_OR_sub("1a - 2")

if __name__ == "__main__":

    unittest.main()