"""Advent of Code 2015 Day 12 Solution
Completed in Jan 2023, reformatted on 29/12/2023"""

import json
import re
from typing import Union, Dict, List

with open("input.json") as f:
    data = json.load(f)

all_numbers = map(int, re.findall(r"-?\d+", str(data)))
print(f"Part 1 Solution: {sum(all_numbers)}")


def sum_no_red(o: Union[int, float, List, str, Dict]) -> int:
    """Sums all numbers in an object if the object doesn't contain the property "red".
    Returns the sum"""
    if isinstance(o, (int, float)):
        return o
    if isinstance(o, str):  # no numbers hidden in strings
        return 0
    if isinstance(o, list):
        return sum(sum_no_red(i) for i in o)
    if isinstance(o, dict):
        if "red" in o.values():
            return 0
        return sum(sum_no_red(i) for i in o.values())


print(f"Part 2 Solution: {sum_no_red(data)}")
