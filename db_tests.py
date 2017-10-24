import unittest
from db import *

class dbTests(unittest.TestCase):
    def test_get_url_from_query(self):
        a = get_url_from_query('chickens')
        self.assertEqual(a, 'https://dannyrosen.net')

if __name__ == '__main__':
    unittest.main()
