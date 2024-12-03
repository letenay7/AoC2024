from util import read_input_lines


def part1(puzzle_input: list[str]) -> int:
    left, right = parse_input(puzzle_input)
    return sum(abs(left[i] - right[i]) for i in range(len(puzzle_input)))


def part2(puzzle_input: list[str]) -> int:
    left, right = parse_input(puzzle_input)
    frequency = {key: right.count(key) for key in left}
    return sum(key * value for key, value in frequency.items())


def parse_input(puzzle_input):
    left = sorted(int(line.split()[0]) for line in puzzle_input)
    right = sorted(int(line.split()[1]) for line in puzzle_input)
    return left, right


if __name__ == '__main__':
    puzzle_input = read_input_lines("input_files/day01.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
