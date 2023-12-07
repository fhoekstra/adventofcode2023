from solver import solver

import unittest


TEST_INPUT = """INPUT"""

EXPECTED = 142


ITERABLE_INPUT = TEST_INPUT.strip().split("\n")


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(EXPECTED, solver(ITERABLE_INPUT))


if __name__ == "__main__":
    unittest.main()
