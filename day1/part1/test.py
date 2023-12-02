from solver import solver

import unittest


TEST_INPUT = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

EXPECTED = 142


def split_into_lines(s: str) -> list[str]:
    return s.split('\n')


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        input = split_into_lines(TEST_INPUT)
        self.assertEqual(EXPECTED, solver(input))


if __name__ == "__main__":
    unittest.main()
