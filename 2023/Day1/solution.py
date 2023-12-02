""" Advent of Code 2023 Day 1 Solution """

# Imports
import re
from typing import List, Dict

# Loading the input line by line
with open("input.txt") as f:
    lines: List[str] = [line.strip() for line in f.readlines()]

# A useful mapping between representations of numbers
numbers: Dict[str, int] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve(lines, part: int) -> int:
    '''Solves the puzzle for the part specified'''
    calibration_sum: int = 0

    assert part in [
        1,
        2,
    ], f"problem has two parts, so part must be either 1 or 2, got {part}"
    if part == 1:
        regex = r"\d"
    elif part == 2:
        # Part two also needs to look for the words for each number
        # in the regex
        regex = "(?=("
        for i, j in numbers.items():
            regex += f"{i}|{j}|"
        regex = regex[:-1] + "))"

    for line in lines:
        # using regex to find all digits in each line
        digits: List[str] = re.findall(regex, line)
        if len(digits) > 0:
            # Converting first and last items into actual digits if necessary
            first = numbers[digits[0]] if digits[0] in numbers.keys() else digits[0]
            last = numbers[digits[-1]] if digits[-1] in numbers.keys() else digits[-1]
            
            # Combining first and last digit and adding to the total sum
            calibration_sum += int(first + last)

    return calibration_sum


print(f"Part 1 Solution = {solve(lines, part=1)}")
print(f"Part 2 Solution = {solve(lines, part=2)}")
