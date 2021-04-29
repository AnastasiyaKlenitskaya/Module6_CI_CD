import unittest
from Calculator import Calculator


# Test cases to test Calulator methods
# You always create  a child class derived from unittest.TestCase class
class TestCalculator(unittest.TestCase):
    # setUp method overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator()

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 6)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
