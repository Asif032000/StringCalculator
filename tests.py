import unittest

from stringCalculator import add


class TestString(unittest.TestCase):
    def test_num_string(self):
        string = ""
        result = add(string)
        self.assertEqual(result, 0)
        

if __name__ == '__main__':
    unittest.main()