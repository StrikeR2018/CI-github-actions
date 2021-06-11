import unittest
import calculator


class TestCase(unittest.TestCase):

    
    def test_add(self):
        self.assertEqual(calculator.add(2, 4), 6)

        
    def test_sub(self):
        self.assertEqual(calculator.subtract(7, 3), 4)

        
    def test_mul(self):
        self.assertEqual(calculator.mulityply(2, 4), 8)

        
    def test_div(self):
        self.assertEqual(calculator.divide(6, 3), 2)


if __name__ == '__main__':
    unittest.main()
