import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "Adding 2 and 3 should equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Adding -1 and 1 should equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "Adding 0 and 0 should equal 0")
        self.assertEqual(self.calc.add(-5, -3), -8, "Adding -5 and -3 should equal -8")
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0, "Adding 1.5 and 2.5 should equal 4.0")

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "Subtracting 3 from 5 should equal 2")
        self.assertEqual(self.calc.subtract(3, 5), -2, "Subtracting 5 from 3 should equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Subtracting 0 from 0 should equal 0")
        self.assertEqual(self.calc.subtract(-2, -3), 1, "Subtracting -3 from -2 should equal 1")
        self.assertEqual(self.calc.subtract(4.5, 1.5), 3.0, "Subtracting 1.5 from 4.5 should equal 3.0")

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "Multiplying 2 by 3 should equal 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "Multiplying -2 by 3 should equal -6")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Multiplying 0 by 5 should equal 0")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Multiplying -2 by -3 should equal 6")
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0, "Multiplying 2.5 by 2 should equal 5.0")

    def test_division(self):
        """Test the division method with valid inputs and division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Dividing 6 by 3 should equal 2.0")
        self.assertEqual(self.calc.divide(-6, 2), -3.0, "Dividing -6 by 2 should equal -3.0")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Dividing 5 by 2 should equal 2.5")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "Dividing 0 by 5 should equal 0.0")
        self.assertIsNone(self.calc.divide(10, 0), "Dividing by 0 should return None")
        self.assertEqual(self.calc.divide(-10, -5), 2.0, "Dividing -10 by -5 should equal 2.0")

if __name__ == '__main__':
    unittest.main()