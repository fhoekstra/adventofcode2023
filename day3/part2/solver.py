from collections.abc import Iterable
from functools import reduce
from typing import Union


GEAR_CHAR = "*"
NUMBER_CHARS = set(str(n) for n in range(10))


def main():
    with open("puzzle_input.txt") as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    puzzle_input = (l for l in puzzle_input if l)
    full_input: list[list[str]] = list(list(line) for line in puzzle_input)
    vert_idx = -1
    gear_map: dict[
        tuple[int, int], list[int]
    ] = DefaultListMap()  # This maps coords of * symbols to numbers around them
    for current_line in full_input:
        vert_idx += 1
        current_digits = ""
        next_to_gear: set[tuple[int, int]] = set()

        for idx, ch in enumerate(current_line):
            if is_number(ch):
                current_digits += ch
                star_coords = gears_coords_in_surrounding_cells(
                    idx, vert_idx, full_input
                )
                next_to_gear = next_to_gear | star_coords

            if not is_number(ch):
                for gear_cand in next_to_gear:
                    gear_map.append_to(gear_cand, int(current_digits))
                current_digits = ""
                next_to_gear = set()

        if current_digits:  # the line ended with digits
            for gear_cand in next_to_gear:
                gear_map.append_to(gear_cand, int(current_digits))

    ratios = (
        reduce(lambda x, y: x * y, lst) for lst in gear_map.values() if len(lst) == 2
    )
    return sum(ratios)


def gears_coords_in_surrounding_cells(
    idx: int,
    vert_idx: int,
    grid: list[list[str]],
) -> set[tuple[int, int]]:
    res = set()
    indices = get_neighbour_indices(idx, vert_idx, len(grid[vert_idx]), len(grid))
    for x, y in indices:
        if grid[y][x] == "*":
            res.add((x, y))
    return res


def get_neighbour_indices(
    idx: int, vert_idx: int, w: int, h: int
) -> list[tuple[int, int]]:
    left_index = idx - 1 if idx > 0 else idx
    right_index = idx + 1 if idx + 1 < w else idx + 1
    top_index = vert_idx - 1 if vert_idx > 0 else vert_idx
    bottom_index = vert_idx + 1 if vert_idx + 1 < h else vert_idx
    neighbours = []
    for x in range(left_index, right_index + 1):
        for y in range(top_index, bottom_index + 1):
            if x == idx and y == vert_idx:
                continue
            neighbours.append((x, y))
    return neighbours


class DefaultListMap(dict[tuple[int, int], list[int]]):
    def append_to(self, key: tuple[int, int], value: int):
        if key not in self:
            self[key] = []
        self[key].append(value)


def is_number(c: str) -> bool:
    return c in NUMBER_CHARS


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
