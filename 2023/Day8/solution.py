"""Advent of Code 2023 Day 8 Solution"""

from typing import List, Tuple, Dict
from itertools import cycle
from math import gcd

with open("input_test.txt") as f:
    instructions, mapping = f.read().split("\n\n")
    mappings: Dict[str, Tuple[str, str]] = {
        i[:3]: (i[7:10], i[12:-1]) for i in mapping.splitlines()
    }


def steps_to_end(start: str, end: str) -> int:
    """Computes the number of steps it takes to go through the input mapping
    from the 'start' string until you reach a string ending with 'end'"""
    pos: str = start
    step_count: int = 0
    for i in cycle(instructions):
        # extract new position based on the mapping
        pos = mappings[pos][0 if i == "L" else 1]
        step_count += 1
        if pos.endswith(end):
            break
    return step_count


print(f"Part 1 Solution: {steps_to_end('AAA', 'ZZZ')}")

# extract all the valid starting nodes
starts: List[str] = [n for n in mappings.keys() if n[-1] == "A"]

# Note that the mapping is cyclical hence the following works
# Check how many steps it takes to reach a string ending with Z
# for the first time
repeats: List[int] = [steps_to_end(pos, "Z") for pos in starts]

# The first time all positions are at Z will be the lowest common
# multiple of their frequency of repetition
lcm = 1
for i in repeats:
    lcm = lcm * i // gcd(lcm, i)

print(f"Part 2 Solution: {lcm}")
