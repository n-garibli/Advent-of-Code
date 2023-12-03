"""Advent of Code 2023 Day 3 Solution"""

# Imports
import re

# Load input line by line
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

symbol_coors = []
for i, line in enumerate(lines):
    for symbol in re.finditer(r"[^.^\d]", line):
        # store the coordinate of each symbol in the input
        # and specify whether it is a star
        symbol_coors.append((i, symbol.start(), symbol.group() == "*"))

all_adj_nums = []  # tracks all numbers adjacent to a symbol
gear_ratios = []
for symbol in symbol_coors:
    x, y, star = symbol
    adj_nums = []
    for line in lines[x - 1 : x + 2]:
        # looking for numbers in lines adjacent to symbol
        for num in re.finditer(r"\d+", line):
            if y in list(range(num.start() - 1, num.end() + 1)):
                adj_nums.append(int(num.group()))

    # These conditions determine whether the symbol is a valid gear
    if len(adj_nums) == 2 and star:
        gear_ratio = adj_nums[0] * adj_nums[1]
        gear_ratios.append(gear_ratio)

    all_adj_nums.extend(adj_nums)

print(f"Part 1 Solution: {sum(all_adj_nums)}")
print(f"Part 2 Solution: {sum(gear_ratios)}")
