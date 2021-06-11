import calculator
import unittest


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_sub_1(self):
        self.assertEqual(calculator.subtract(4, 3), 1)

    def test_mul_1(self):
        self.assertEqual(calculator.mulityply(3, 4), 12)

    def test_div_1(self):
        self.assertEqual(calculator.divide(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
