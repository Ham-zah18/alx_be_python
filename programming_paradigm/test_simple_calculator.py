import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 10), 15)
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, -10), 5)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(5, 10), 50)
        self.assertEqual(self.calc.multiply(-5, -10), 50)


    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, -5), 2)

    def test_division_by_zero(self):
        #Test division by zero.
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()