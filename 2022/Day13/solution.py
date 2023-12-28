"""Advent of Code 2022 Day 13 Solution
Completed in 2022, reformatted (and part 2 rewritten) on 28/12/2023"""

from typing import List, Union, Optional
from itertools import zip_longest
from ast import literal_eval
from functools import cmp_to_key
from math import prod

with open("input.txt") as f:
    # All information split by monkeys
    items: List[Union[List, int]] = [
        literal_eval(i) for i in f.read().splitlines() if i != ""
    ]


def compare(
    left: Optional[Union[List, int]] = None, right: Optional[Union[List, int]] = None
) -> Optional[bool]:
    """Returns True if left item needs to come before the right item as per the rules
    specified in the problem, otherwise returns False. Returns None if the order cannot
    be determined"""
    if left is None: 
         # happens only during recursion if left is a list and ran out of items
        return True
    if right is None:  
        # happens only during recursion if right is a list and ran out of items
        return False

    if isinstance(left, int) and isinstance(right, int):  # comparing two integers
        if left < right:
            return True
        if right < left:
            return False
        return None
    # Make non list item into a list
    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    for l, r in zip_longest(left, right):
        output = compare(l, r)
        if output is not None:
            return output


print(f"Part 1 Solution: {sum(compare(items[i], items[i+1]) * int((i+2)/2) for i in range(0,len(items),2))}")

dividers: List = [[[2]], [[6]]]
sorted_items = sorted(
    items + dividers, key=cmp_to_key(lambda x, y: -1 if compare(x, y) else 1)
)

print(f"Part 2 Solution: {prod([sorted_items.index(i)+1 for i in dividers])}")
