from collections.abc import Iterable

ORD_0 = ord('0')
ORD_9 = ord('9')

DIGITS_FWD = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
DIGITS_BWD = {
        k[::-1]: v
        for k, v in DIGITS_FWD.items()
        }
STARTING_LETTER_OF_DIGITS_FWD = {k[0] for k in DIGITS_FWD.keys()}
STARTING_LETTER_OF_DIGITS_BWD = {k[0] for k in DIGITS_BWD.keys()}


def main():
    with open('puzzle_input.txt') as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    som = 0
    for line in puzzle_input:
        if not line:
            continue
        som += first_digit(line)*10 + last_digit(line)
    return som


def is_digit(c: str) -> bool:
    return ORD_0 <= ord(c) <= ORD_9


def first_digit(line: str,):
    return find_digit(line, DIGITS_FWD, STARTING_LETTER_OF_DIGITS_FWD)


def find_digit(line: str,
               digits_dict: dict[str, int],
               starting_letters: set[str]) -> int:
    for idx, c in enumerate(line):
        if is_digit(c):
            return int(c)
        if c in starting_letters:
            for digit_word in digits_dict.keys():
                if line[idx:].startswith(digit_word):
                    return digits_dict[digit_word]
    raise ValueError(f"There is no digit in this line: {line}")


def last_digit(line: str) -> int:
    return find_digit(line[::-1],
                      DIGITS_BWD,
                      STARTING_LETTER_OF_DIGITS_BWD)


if __name__ == "__main__":
    main()
