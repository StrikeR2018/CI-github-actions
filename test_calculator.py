import unittest
import calculator

class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(calculator.add(2, 4), 6)

    def test_sub_1(self):
        self.assertEqual(calculator.subtract(7, 3), 4)

    def test_mul_1(self):
        self.assertEqual(calculator.mulityply(2, 4), 8)

    def test_div_1(self):
        self.assertEqual(calculator.divide(6, 3), 2)


if __name__ == '__main__':
    unittest.main()
