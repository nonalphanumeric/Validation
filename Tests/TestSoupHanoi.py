import unittest
from Hanoi.SoupHanoi import SoupHanoi


class MyTestCase(unittest.TestCase):
    def test_initial_conf(self):
        hanoi = SoupHanoi()
        self.assertEqual(hanoi.initialConf(), [[[1, 2, 3],[], []]])

    def test_next(self):
        soup = SoupHanoi()
        res = []
        for rule in soup.enabledActions([[1, 2, 3], [], []]):
            print(str(rule) + " is enabled")
            res.append(soup.execute(rule, [[1, 2, 3], [], []]))
        self.assertEqual(res, [[[[[1, 2], [3], []]]], [[[[1, 2], [], [3]]]]])

if __name__ == '__main__':
    unittest.main()
