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

EXPECTED = 4361

ITERABLE_INPUT = TEST_INPUT.strip().split("\n")


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(EXPECTED, solver(ITERABLE_INPUT))

    def test_my_added_example(self):
        input = """
123....4
*...7.$.
.55.....
...#....
........
....9*11
345.....
"""
        input = input.strip().split("\n")
        self.assertEqual(202, solver(input))


if __name__ == "__main__":
    unittest.main()
