"""Advent of Code 2015 Day 13 Solution
Completed on 11/01/2023, reformatted on 29/12/2023"""

from itertools import permutations
from typing import Dict, Tuple, List
from collections import defaultdict

# Stores the names of everyone invited to dinner
people: List[str] = []
# Stores happiness change if a given pair of people sit next to each other
all_opinions: Dict[Tuple[str, str], int] = defaultdict(lambda: 0)

with open("input.txt") as f:
    for i in f.read().splitlines():
        i = i.split(" ")
        if i[0] not in people:
            people.append(i[0])
        people_combo = (i[0], i[-1][:-1])  # sliced second name to remove .
        happiness = int(i[3]) * (1 if i[2] == "gain" else -1)
        all_opinions[people_combo] += happiness
        all_opinions[people_combo[::-1]] += happiness


def find_max_happiness(names: List[str], opinions: Dict[Tuple[str, str], int]) -> int:
    """Returns the maximum possible happiness when arranging people
    with names as in 'names'"""
    max_happiness = 0
    for a in permutations(names):
        # Sums everyones happiness by considering every pair
        h = sum(opinions[(a[i], a[i - 1])] for i in range(len(a))[::-1])
        max_happiness = max(max_happiness, h)
    return max_happiness


print(f"Part 1 Solution: {find_max_happiness(people, all_opinions)}")
print(f"Part 2 Solution: {find_max_happiness(people + ['me'], all_opinions)}")
