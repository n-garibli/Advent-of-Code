"""Advent of Code 2022 Day 1 Solution
Completed in 2022, rewritten on 6/12/2023"""

from typing import List

with open("input_test.txt") as f:
    # Parsing input to extract a list of inventories (one per reindeer)
    inventories: List[List[int]] = [
        list(map(int, x.splitlines())) for x in f.read().split("\n\n")
    ]

cals_per_elf: List[int] = [sum(i) for i in inventories]
print(f"Part 1 Solution: {max(cals_per_elf)}")

cals_per_elf.sort()
print(f"Part 2 Solution: {sum(cals_per_elf[-3:])}")
