import unittest

from NbBits.nbBits import NbBits


class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        nb = NbBits(6)
        self.assertEqual(nb.k, 6)

    def test_roots(self):
        nb = NbBits(6)
        self.assertEqual(nb.roots(), 0)

    def test_next_roots(self):
        nb = NbBits(6)
        self.assertEqual(nb.next(0), [1, 2, 4, 8, 16, 32])




if __name__ == '__main__':
    unittest.main()
