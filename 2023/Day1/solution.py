""" Advent of Code 2023 Day 1 Solution """
import re
from typing import List, Dict

# Loading the input line by line
with open("input_test.txt") as f:
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


def solve(lines: List[str], regex: str) -> int:
    '''Solves the puzzle using regex specified - the regex indicates
    which patterns in each line of the input are considered digits
    '''
    calibration_sum: int = 0

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

regex = r"\d"
print(f"Part 1 Solution: {solve(lines, regex=regex)}")

regex = "(?=("
for i, j in numbers.items():
    regex += f"{i}|{j}|"
regex = regex[:-1] + "))"

print(f"Part 2 Solution: {solve(lines, regex=regex)}")
