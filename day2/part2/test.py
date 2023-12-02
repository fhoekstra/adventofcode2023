from solver import hand_parse, solver

import unittest


TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

EXPECTED = 2286


def split_into_lines(s: str) -> list[str]:
    return s.split("\n")


class TestBasicExample(unittest.TestCase):
    def test_basic_example(self):
        input = split_into_lines(TEST_INPUT)
        self.assertEqual(EXPECTED, solver(input))

    def test_parsing_of_cube_results(self):
        input = "3 blue, 4 red"
        output = hand_parse(input)
        self.assertEqual([4, 0, 3], output)


if __name__ == "__main__":
    unittest.main()
