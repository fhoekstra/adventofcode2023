from collections.abc import Iterable
from functools import reduce


def main():
    with open("puzzle_input.txt") as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    som = 0
    for line in puzzle_input:
        _, cube_results = line.split(": ")
        power = cube_power(cube_results)
        som += power
    return som


def cube_power(cube_results: str) -> int:
    subsets = cube_results.split("; ")
    minimums_rgb = hand_parse(subsets[0])
    for cube_csv in subsets:
        nums = hand_parse(cube_csv)
        minimums_rgb = tuple(max(el[0], el[1]) for el in zip(minimums_rgb, nums))
    return reduce(lambda left, right: left * right, minimums_rgb)


def hand_parse(cube_csv: str) -> list[int]:
    res = [0, 0, 0]
    colors = cube_csv.split(", ")
    for c_s in colors:
        idx = None
        num, name = c_s.split()
        match name:
            case "red":
                idx = 0
            case "green":
                idx = 1
            case "blue":
                idx = 2
        res[idx] = int(num)
    return res


if __name__ == "__main__":
    main()
