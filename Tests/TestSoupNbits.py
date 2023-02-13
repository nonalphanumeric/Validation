import unittest
from NbBits.SoupNBits import SoupNBits

class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        nbits = SoupNBits()
        self.assertEqual(nbits.initialConf(), [0])

    def test_next(self):
        soup = SoupNBits()
        res = []
        for rule in soup.enabledActions(0):
            print(str(rule) + " is enabled")
            res.append(soup.execute(rule, 0))
        self.assertEqual(res, [[1], [2], [4]])



if __name__ == '__main__':
    unittest.main()
