from solver import solver

import unittest


TEST_INPUT = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

EXPECTED = 281


def split_into_lines(s: str) -> list[str]:
    return s.split('\n')


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        input = split_into_lines(TEST_INPUT)
        self.assertEqual(EXPECTED, solver(input))


if __name__ == "__main__":
    unittest.main()
