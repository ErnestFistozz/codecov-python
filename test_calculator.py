
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_constructor_values(self):
        cal = Calculator(1, 2)
        self.assertEqual(cal.x, 1)
        self.assertEqual(cal.y, 2)


if __name__ == '__main__':
    unittest.main()