from collections.abc import Iterable

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def main():
    with open('puzzle_input.txt') as f:
        print(solver(f))


def solver(puzzle_input: Iterable[str]) -> int:
    som = 0
    for line in puzzle_input:
        game_str, cube_results = line.split(':')
        game_num = int(game_str.lstrip('Game '))
        possible = cube_test(cube_results)
        if possible:
            som += game_num
    return som


def cube_test(cube_results: str) -> bool:
    subsets = cube_results.split(';')
    for cube_csv in subsets:
        colors = cube_csv.strip().split(', ')
        for c_s in colors:
            num, name = c_s.split(' ')
            if int(num) <= 12:
                continue
            if over_max(int(num), name):
                return False
    return True


def over_max(num: int, name: str) -> bool:
    if (n := name.lower()) in {"red", "green", "blue"}:
        if n == "red":
            return num > MAX_RED
        if n == "green":
            return num > MAX_GREEN
        if n == "blue":
            return num > MAX_BLUE
    raise ValueError(f"Unkown color: {name}")


if __name__ == "__main__":
    main()

