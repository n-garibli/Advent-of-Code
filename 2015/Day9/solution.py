"""Advent of Code 2015 Day 9 Solution
Note: this can be shorter and easier with networkx and the input
is small enough to not need some of the optimisations but I 
wanted to practice some simple dynamic programming 
"""

from typing import Dict, List, Tuple
from itertools import permutations

# Stores distances for possible paths taken
paths: Dict[Tuple[str], int] = {}

# Stores all locations that must be visited
locs: List[str] = []
with open("input_test.txt") as f:
    for line in f.readlines() :
        loc1, loc2, dist = line.strip().split(" ")[::2]
        locs.extend([loc for loc in [loc1, loc2] if loc not in locs])
        paths[(loc1, loc2)] = int(dist)
        paths[(loc2, loc1)] = int(dist)

min_path = float("inf")
max_path = 0
for ordered_locs in list(permutations(locs)):
    if ordered_locs in paths.keys():
        # Check if this has already been computed
        path_length = paths[ordered_locs]
    else :
        path_length = 0 
        for i in range(len(ordered_locs) - 1):
            path_length += paths[(ordered_locs[i], ordered_locs[i + 1])]
        # Stores the computed values to avoid recalculating in the future
        paths[ordered_locs] = path_length
        paths[ordered_locs[::-1]] = path_length
    
    if path_length < min_path:
        min_path = path_length
    if path_length > max_path:
        max_path = path_length

print(f"Part 1 Solution: {min_path}")
print(f"Part 2 Solution: {max_path}")
