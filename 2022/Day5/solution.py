"""Advent of Code 2022 Day 6 Solution"""

import re
from typing import List
from copy import deepcopy

with open("input_test.txt") as f:
    box_positions, instructions = f.read().split("\n\n")

# This will have a list representing each stack (in order). Each stack list
# will contain the crates that are stacked in that stack (last element is
# the top crate)
stacks: List[List[str]] = []
lines = box_positions.splitlines()

for stack_id in re.findall(r"\d+", lines[-1]):
    r = lines[-1].index(stack_id)
    stacks.append([x[r] for x in lines[:-1][::-1] if x[r] != " "])

# stacks2 will be moved by CrateMover 9001 instead of 9000
# Using deepcopy to avoid list mutability problems
stacks2 = deepcopy(stacks)

for i in instructions.splitlines():
    n_crates, start, end = [int(j) for j in re.findall(r"\d+", i)]

    # add n_crates from start stack to end stack
    stacks[end - 1].extend(stacks[start - 1][-n_crates:][::-1])
    stacks2[end - 1].extend(stacks2[start - 1][-n_crates:])

    # remove the n_crates from start stack
    for j in range(1, n_crates + 1):
        stacks[start - 1].pop()
        stacks2[start - 1].pop()

print(f"Part 1 Solution: {''.join([i[-1] for i in stacks])}")
print(f"Part 2 Solution: {''.join([i[-1] for i in stacks2])}")
