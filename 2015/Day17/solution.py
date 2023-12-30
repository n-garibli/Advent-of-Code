"""Advent of Code 2015 Day 17 Solution
Completed on 11/01/2023, reformatted on 30/12/2023."""

from typing import List
from itertools import combinations

with open("input.txt") as f:
    containers: List[int] = list(map(int, f.readlines()))

count: int = 0
search_pt2: bool = True
for i in range(1, len(containers)):
    combos: List[List[int]] = list(combinations(containers, i))
    n_valid: int = sum(sum(c) == 150 for c in combos)
    if n_valid > 0 and search_pt2:
        # first time we have enough containers for 150l of eggnog
        print(f"Part 2 Solution: {n_valid}")
        search_pt2 = False
    elif not search_pt2 and n_valid == 0:
        # optimisation: at this point we have too many containers so we get too much eggnog
        # no need to consider arrangements with even more containers
        break
    count += n_valid

print(f"Part 1 Solution: {count}")
