"""Advent of Code 2022 Day 4 Solution"""

from typing import List

with open("input_test.txt") as f:
    ranges: List[str] = [pair.split(",") for pair in f.read().splitlines()]

full_overlap: int = 0
partial_overlap: int = 0

for range_pair in ranges:
    r1, r2 = [tuple(map(int, r.split("-"))) for r in range_pair]

    r1: set = set(range(r1[0], r1[1] + 1))
    r2: set = set(range(r2[0], r2[1] + 1))

    intersect: set = r1.intersection(r2)

    if len(intersect) > 0:
        partial_overlap += 1
        if intersect == r1 or intersect == r2:
            full_overlap += 1

print(f"Part 1 Solution: {full_overlap}")
print(f"Part 2 Solution: {partial_overlap}")
