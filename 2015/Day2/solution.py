"""Advent of Code 2015 Day 2 Solution
Completion Date: 25/12/2013"""

from typing import List

with open("input_test.txt") as f:
    # load and parse the input
    p_dims: List[List[int]] = [map(int, i.split("x")) for i in f.read().splitlines()]

total_paper: int = 0
total_ribbon: int = 0
for dims in p_dims:
    l, w, h = dims
    side_areas: List[int] = [l * w, w * h, l * h]
    total_paper += min(side_areas) + 2 * sum(side_areas)
    ribbon_to_wrap: int = min([2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l])
    total_ribbon += ribbon_to_wrap + l * w * h  # add ribbon for bow too

print(f"Part 1 Solution: {total_paper}")
print(f"Part 2 Solution: {total_ribbon}")
