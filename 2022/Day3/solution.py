"""Advent of Code 2022 Day 3 Solution"""

from string import ascii_lowercase as lc, ascii_uppercase as uc
from typing import List

with open("input.txt") as f:
    items: List[str] = f.read().splitlines()


def common_item_p(inputs: List[str]) -> int:
    '''Given a list of strings, this function returns the 'priority' of
    the only element present in all strings'''
    common_item = set(inputs[0])
    for i in inputs[1:]:
        common_item = common_item.intersection(i)
    priority = (lc + uc).index(list(common_item)[0]) + 1
    return priority


p1 = sum([common_item_p([i[: int(len(i) / 2)], i[int(len(i) / 2) :]]) for i in items])
p2 = sum([common_item_p([items[i], items[i + 1], items[i + 2]]) for i in range(0, len(items), 3)])

print(f"Part 1 Solution: {p1}")
print(f"Part 2 Solution: {p2}")
