import unittest
from calculator import calculate  # Assuming the script is named calculator.py

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("add", 2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate("subtract", 10, 4), 6)

    def test_division_by_zero(self):
        self.assertEqual(calculate("divide", 5, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()
