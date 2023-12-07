from collections.abc import Iterable
from collections import defaultdict


def main():
    with open("puzzle_input.txt") as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    cards: dict[int, int] = defaultdict(lambda: 1)
    for line in puzzle_input:
        card_num, winning, have = card_parse(line)
        if card_num not in cards:
            cards[card_num] = 1
        matches = len(winning & have)
        if matches:
            multiples = cards[card_num]
            for c in range(card_num + 1, card_num + matches + 1):
                cards[c] += multiples
    return sum(num for num in cards.values())


def card_parse(line: str) -> tuple[int, set[int], set[int]]:
    card_name, numbers_str = line.split(":")
    card_num = int(card_name.split(" ")[-1])
    winning_s, have_s = numbers_str.split("|")
    return card_num, numbers_parse(winning_s), numbers_parse(have_s)


def numbers_parse(s: str) -> set[int]:
    return set(int(x) for x in s.split(" ") if len(x))


if __name__ == "__main__":
    main()
