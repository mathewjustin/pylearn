from basics.functions import n_factorial
import unittest

class TestNFactorial(unittest.TestCase):
    def testRecursion(self):
        self.assertEqual(n_factorial.factorial(5),120)



