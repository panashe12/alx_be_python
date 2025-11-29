import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertEqual(self.calc.add(2.5, 2.5), 5.0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10.5, 0.5), 10.0)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """Test the divide method including divide-by-zero."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(5, -1), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(3.5, 0.5), 7.0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
