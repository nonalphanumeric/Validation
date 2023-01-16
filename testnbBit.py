import unittest
from nbBits import NbBits


class TestNbBits(unittest.TestCase):
    """ Test la methode next() de nbBits"""

    def test_next(self):
        nb = NbBits(2)
        for res in nb.next(nb.roots()):
            result = format(res, '#0{}b'.format(nb.k + 2))
            return self.assertTrue(result == '0b10' or result == '0b01')

    """ Test  flipnthbit """

    def test_flipnthbit(self):
        nb = NbBits(2)
        m = 0;
        n = 1;
        return self.assertEqual(nb.flipnthbit(m, n), 2)


if __name__ == "__main__":
    unittest.main()
