import unittest

def add_numbers(a, b):
    return a + b

class testFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(4, 5)
        self.assertEqual(result, 9)
    
    def test_addition_negative_numbers(self):
        result = add_numbers(6, -2)
        self.assertEqual(result, 4)

    def test_addition_float_numbers(self):
        result = add_numbers(1.5, 2.5)
        self.assertAlmostEquals(result, 4.0, places=2 )

if __name__ == '__main__':
    unittest.main()

