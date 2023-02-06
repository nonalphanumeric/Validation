from _pytest import unittest

from Hanoi.HanoiRules import HanoiRules

class TestHanoiRules:
    def test_next(self):
        hr = HanoiRules()

if __name__ == "__main__":
    unittest.main()
