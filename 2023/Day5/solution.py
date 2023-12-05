"""Advent of Code 2023 Day 5 Solution
Not brute force - runs quite fast!"""

import re
from typing import List, Tuple, Dict, Optional
from collections import defaultdict

# This dictionary will store all the source ranges in the form variable_id : [(start,end),..]
# In this script the variable_id (var_id) is a number assigned to each variable
# (seed = 0, soil=1, location=7)
src_ranges: Dict[int, List[Tuple[int, int]]] = defaultdict(lambda: [])

# Stores the destination for the start of each source range for each var_id
dsts: Dict[int, List] = defaultdict(lambda: [])

with open("input.txt") as f:
    # extract all seeds as integers
    seeds = list(map(int, re.findall(r"\d+", f.readlines(1)[0])))

    # var_info in this loop is of the form ['dst src r','dst src r',...]
    for var_id, var_info in enumerate(
        [x.split(":")[1].splitlines()[1:] for x in f.read().split("\n\n")]
    ):
        for mapping in var_info:
            dst, src, r = map(int, mapping.split())
            src_ranges[var_id + 1].append((src, src + r))
            dsts[var_id + 1].append(dst)


def find_location(x: Tuple[int, int], var_id: Optional[int] = 0) -> int:
    """Maps the values for var_id in the range (x[0],x[1]),
    to their location and returns the minimum location."""

    if var_id + 1 >= 8:
        # there are only 8 variables, hence var_id=7 represents the last variable (location)
        # Since x representa a range of values for the variable, the first element is
        # the smallest, by definition.
        return x[0]

    # Stores args that need to be inputted into find_location() again
    new_inputs: List[Dict] = []

    # iterate through all ranges for the variable
    for i, src_range in enumerate(src_ranges[var_id + 1]):
        dst = dsts[var_id + 1][i]
        if x[0] >= src_range[0] and x[0] < src_range[1]:
            new_x_0 = dst + (x[0] - src_range[0])
            if src_range[1] < x[1]:
                # input range does not fully lie within src range, hence will
                # need to find another mapping for this var_id
                # for the remainder of the input range
                new_inputs.append({"x": (src_range[1], x[1]), "var_id": var_id})
                new_x_1 = dst + src_range[1] - src_range[0]
            else:
                # input range fully lies within src_range, extracting new mapping
                new_x_1 = dst + x[1] - src_range[0]

            new_inputs.append({"x": (new_x_0, new_x_1), "var_id": var_id + 1})
            break
    if not new_inputs:
        # suggests that no value in the input range (x) is in any of the source ranges
        # for the given variable. Moving on to the next variable.
        new_inputs.append({"x": x, "var_id": var_id + 1})

    # Search for the minimum location
    loc = min([find_location(**args) for args in new_inputs])

    return loc


print(f"Part 1 Solution: {min([find_location((s,s)) for s in seeds])}")
print(f"Part 2 Solution: {min([find_location((s,s + r)) for s, r in zip(seeds[::2], seeds[1::2])])}")
