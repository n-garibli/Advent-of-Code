"""Advent of Code 2015 Day 24 Solution
Completed on 01/01/2024"""

from typing import List
from itertools import combinations
from math import prod

with open("input.txt") as f:
    weights: List[int] = list(map(int, f.read().splitlines()))


def get_min_QE(weights: List[int], n_groups: int) -> int:
    """Returns minimum quantum entaglement of smallest group when splitting
    packages into 'n_groups' groups of equal weight, where 'weights' contains
    the weights of all packages to consider."""
    target_sum: int = sum(weights) / n_groups  # each group total weight must be this
    for n in range(len(weights)):
        possible_group1s: List[List[int]] = [
            c for c in combinations(weights, n) if sum(c) == target_sum
        ]  # all possible smallest groups given that the smallest group is of size n
        if len(possible_group1s) == 0:
            # impossible to have so few packages in one group
            continue
        return min(prod(c) for c in possible_group1s) # min QE


print(f"Part 1 Solution: {get_min_QE(weights,3)}")
print(f"Part 2 Solution: {get_min_QE(weights,4)}")
