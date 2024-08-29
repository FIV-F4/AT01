import unittest
from main import *

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(-1, 1), 3)
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertNotEqual(subtract(4, 2), 1)
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertNotEqual(multiply(4, 5), 12)
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertNotEqual(divide(10, 2), 0)

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertFalse(check(3))
        self.assertTrue(not check(4))
class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
    def test_divide_fail(self):
        self.assertRaises(ValueError, divide, 10, 0)

class TestOstatok(unittest.TestCase):
    def test_ostatok(self):
        self.assertEqual(ostatok(10, 3), 1)
        self.assertNotEqual(ostatok(10, 3), 0)
    def test_ostatok_fail(self):
        self.assertRaises(ValueError, ostatok, 10, 0)
        self.assertEqual(ostatok(10, 0), 1)

if __name__ == '__main__':
    unittest.main()