"""Advent of Code 2023 Day 15 Solution"""

from typing import List, Dict, Optional
from collections import defaultdict


with open("input.txt") as f:
    strs: List[str] = f.read().split(",")


def hashify(s: str):
    """Applies reindeer HASH encoding to a string"""
    current_val = 0
    for x in s:
        current_val += ord(x)
        current_val *= 17
        current_val %= 256
    return current_val


print(f"Part 1 Solution: {sum([hashify(s) for s in strs])}")

# will store a list of ordered lenses (value) that each box (key) contains
boxes: Dict[int, List[str]] = defaultdict(lambda: [])
# will store the focal length of each lens
f_lengths: Dict[str, int] = {}
# will store the box id where each lens is located
f_locs: Dict[str, Optional[int]] = {}

# This loop populates all the dictionaries above
for s in strs:
    if s[-1] == "-":
        label: str = s[:-1]
        box_id: int = hashify(s[:-1])
        if label in boxes[box_id]:
            boxes[box_id].remove(label)
            f_locs[label] = None
    else:
        label, f = s.split("=")
        box_id = hashify(label)
        f_lengths[label] = int(f)
        if label not in boxes[box_id]:
            boxes[box_id].append(label)
            f_locs[label] = box_id

total_f_power: int = 0
# This loop computes total_f_power
for label, f in f_lengths.items():
    if f_locs[label] is not None:
        box_id = f_locs[label]
        order_in_box = boxes[box_id].index(label) + 1
        f_power = (box_id + 1) * order_in_box * f
        total_f_power += f_power

print(f"Part 2 Solution: {total_f_power}")
