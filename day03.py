from util import *
import re


def get_result(multiplications: list[str]) -> int:
    result = 0
    for multiplication in multiplications:
        numbers = [int(num) for num in re.findall(r'\d+', multiplication)]
        result += numbers[0] * numbers[1]
    return result


def part1(puzzle_input: str) -> int:
    regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    multiplications = re.findall(regex, puzzle_input)
    return get_result(multiplications)


def part2(puzzle_input: str) -> int:
    regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    multiplications = []
    enabled = True
    matches = re.findall(regex, puzzle_input)
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                multiplications.append(match)
    return get_result(multiplications)


if __name__ == '__main__':
    puzzle_input = read_input_as_string("input_files/day03.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
