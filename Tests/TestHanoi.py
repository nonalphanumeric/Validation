import unittest
from Hanoi.HanoiRules import HanoiRules

class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        hanoi = HanoiRules()
        self.assertEqual(hanoi.initial, [[1, 2, 3],[], []])

    def test_next(self):
        hanoi = HanoiRules()
        self.assertEqual(hanoi.next([[1, 2, 3],[], []]), [[[1, 2], [3], []], [[1, 2], [], [3]]])


if __name__ == '__main__':
    unittest.main()
