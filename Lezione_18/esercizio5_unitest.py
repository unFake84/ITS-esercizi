import unittest
from esercizio5 import sum_OR_sub, FormulaError

class Testsum_OR_sub(unittest.TestCase):

    def test_addition(self):

        self.assertEqual(sum_OR_sub("3 + 2"), 5.0)

    def test_subtraction(self):

        self.assertEqual(sum_OR_sub("10 - 7"), 3.0)

    def test_invalidOperator(self):

        with self.assertRaises(FormulaError):
            
            sum_OR_sub("1 & 2")

    def test_missingNumber(self):

        with self.assertRaises(FormulaError):

            sum_OR_sub("1 +")

if __name__ == "__main__":

    unittest.main()