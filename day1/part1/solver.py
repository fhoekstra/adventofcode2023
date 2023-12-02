
from collections.abc import Iterable, Sequence

ORD_0 = ord('0')
ORD_9 = ord('9')


def main():
    with open('puzzle_input.txt') as f:
        print(solver(f))


def solver(puzzle_input: Iterable[Sequence[str]]) -> int:
    som = 0
    for l in puzzle_input:
        som += first_digit(l)*10 + last_digit(l)
    return som


def filter_digit(c: str) -> bool:
    return ORD_0 <= ord(c) <= ORD_9


def first_digit(line: Iterable[str]) -> int:
    digit_char = next(filter(filter_digit, line), '0')
    return int(digit_char)


def last_digit(line: Sequence[str]) -> int:
    return first_digit(reversed(line))


if __name__ == "__main__":
    main()
