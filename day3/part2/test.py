from solver import solver

import unittest


TEST_INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

EXPECTED = 467835

ITERABLE_INPUT = TEST_INPUT.strip().split("\n")


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(EXPECTED, solver(ITERABLE_INPUT))


if __name__ == "__main__":
    unittest.main()
