from util import read_input


def tolerate_one_fault(level: list[int]) -> bool:
    for i in range(len(level)):
        fault = level.copy()
        fault.pop(i)
        if check_level(fault):
            return True
    return False



def check_differences(level: list[int]) -> bool:
    for i in range(len(level) - 1):
        difference = abs(level[i] - level[i + 1])
        valid = 1 <= difference <= 3
        if not valid:
            return False
    return True


def check_level(level: list[int]) -> bool:
    return check_increasing(level) and check_differences(level)


def check_increasing(level: list[int]) -> bool:
    return level == sorted(level) or level == sorted(level, reverse=True)


def part1(puzzle_input: list[str]) -> int:
    safe = 0
    for row in puzzle_input:
        level = [int(element) for element in row.split()]
        if check_level(level):
            safe += 1
    return safe


def part2(puzzle_input: list[str]) -> int:
    safe = 0
    for row in puzzle_input:
        level = [int(element) for element in row.split()]
        if tolerate_one_fault(level):
            safe += 1
    return safe


if __name__ == '__main__':
    puzzle_input = read_input("input_files/day02.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
