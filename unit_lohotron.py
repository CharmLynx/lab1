import unittest
from lohotron import check

class MyTestCase(unittest.TestCase):
    def test_check_loh(self):
        self.assertEqual(check(2), "loh")

if __name__ == '__main__':
    unittest.main()
