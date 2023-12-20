"""Advent of Code 2015 Day 2 Solution"""

from typing import List

with open("input_test.txt") as f:
    # load and parse the input
    present_dims: List[List[str]] = [line.strip().split("x") for line in f.readlines()]

total_paper: int = 0
total_ribbon: int = 0
for dims in present_dims:
    l, w, h = [int(d) for d in dims]
    side_areas: List[int] = [l * w, w * h, l * h]
    paper_needed = min(side_areas) + 2 * sum(side_areas)
    ribbon_to_wrap = min([2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l])
    ribbon_for_bow = l * w * h
    total_paper += paper_needed
    total_ribbon += ribbon_to_wrap + ribbon_for_bow

print(f"Part 1 Solution: {total_paper}")
print(f"Part 2 Solution: {total_ribbon}")
