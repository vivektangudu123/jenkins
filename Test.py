import unittest
from lcm import lcm
class Testlcm(unittest.TestCase):
    def test_lcm1(self):
        result = lcm(5,2)
        self.assertEqual(result,10)
    def test_lcm2(self):
        result = lcm(2,4)
        self.assertEqual(result,4)
    def test_lcm3(self):
        result = lcm(7,3)
        self.assertEqual(result,21)
    def test_lcm4(self):
        result = lcm(10,5)
        self.assertEqual(result,5)
    def test_lcm5(self):
        result = lcm(100, 10)
        self.assertEqual(result,10)

if __name__ == '__main__':
    unittest.main()
