import unittest

from stringCalculator import add


class TestString(unittest.TestCase):
    def test_num_string(self):
        
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1,5"), 6)
        

if __name__ == '__main__':
    unittest.main()