from collections.abc import Iterable


def main():
    with open("puzzle_input.txt") as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    som = 0
    for line in puzzle_input:
        winning, have = card_parse(line)
        matches: set[int] = winning & have
        if matches:
            som += 2 ** (len(matches) - 1)
    return som


def card_parse(line: str) -> tuple[set[int], set[int]]:
    card_name, numbers_str = line.split(":")
    winning_s, have_s = numbers_str.split("|")
    return numbers_parse(winning_s), numbers_parse(have_s)


def numbers_parse(s: str) -> set[int]:
    return set(int(x) for x in s.split(" ") if len(x))


if __name__ == "__main__":
    main()
