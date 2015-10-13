__author__ = 'PipinYusmar'

import unittest
import Main.PMi

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Main.PMi.listSize([]), 0)


if __name__ == '__main__':
    unittest.main()