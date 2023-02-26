
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_constructor_values(self):
        cal = Calculator(1, 2)
        self.assertEqual(cal.x, 1)
        self.assertEqual(cal.y, 2)

    def test_addition(self):
        cal = Calculator(5, 2)
        self.assertEqual(cal.add(), 7)

    def test_subtraction(self):
        cal = Calculator(8, 3)
        self.assertEqual(cal.subtract(), 5)


    def test_multiplication(self):
        cal = Calculator(-2, 3)
        self.assertEqual(cal.multiply(), -6)
    
    def test_modulus(self):
        cal = Calculator(8, 4)
        self.assertEqual(cal.modulus(), 0)

if __name__ == '__main__':
    unittest.main()