from collections.abc import Iterable


FILLER_CHAR = "."
NUMBER_CHARS = set(str(n) for n in range(10))
NON_SYMBOL_CHARS = set([str(n) for n in range(10)] + [FILLER_CHAR, "\n"])


def main():
    with open("puzzle_input.txt") as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    puzzle_input = (l for l in puzzle_input if l)
    full_input: list[list[str]] = list(list(line) for line in puzzle_input)
    som = 0
    for last_line, current_line, next_line in zip(
        top_pad(FILLER_CHAR, full_input),
        full_input,
        bottom_pad(FILLER_CHAR, full_input)[1:],
    ):
        current_digits = ""
        is_part = False
        for idx, ch in enumerate(current_line):
            if is_number(ch):
                current_digits += ch
                if symbol_in_surrounding_cells(idx, last_line, current_line, next_line):
                    is_part = True
            if not is_number(ch):
                if is_part:
                    som += int(current_digits)
                current_digits = ""
                is_part = False
        if current_digits:  # the line ended with digits
            if is_part:
                som += int(current_digits)
    return som


def symbol_in_surrounding_cells(
    idx: int, last_line: list[str], current_line: list[str], next_line: list[str]
) -> bool:
    left_index = idx - 1 if idx > 0 else idx
    right_index = idx + 2 if idx + 1 < len(current_line) else idx + 1
    cells_to_check: list[str] = (
        last_line[left_index:right_index]
        + current_line[left_index:right_index]
        + next_line[left_index:right_index]
    )
    return any(
        filter(
            is_symbol,
            cells_to_check,
        )
    )


def is_number(c: str) -> bool:
    return c in NUMBER_CHARS


def is_symbol(c: str) -> bool:
    return c not in NON_SYMBOL_CHARS


def top_pad(c: str, block: list[list[str]]) -> list[list[str]]:
    top_pad_line = [c for _ in range(len(block[0]))]
    res = [top_pad_line]
    res.extend(block)
    return res


def bottom_pad(c: str, block: list[list[str]]) -> list[list[str]]:
    bottom_pad_line = [c for _ in range(len(block[-1]))]
    res = block[:]
    res.append(bottom_pad_line)
    return res


if __name__ == "__main__":
    main()
