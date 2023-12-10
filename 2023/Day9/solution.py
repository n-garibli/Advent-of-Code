"""Advent of Code 2023 Day 9 Solution"""

import re
from typing import List, Union
import numpy as np

with open("input.txt") as f:
    histories: List[List[int]] = [
        list(map(int, re.findall(r"-?\d+", h))) for h in f.read().splitlines()
    ]


def find_val(seq: Union[List[int], np.array], prev=False) -> int:
    """Looks for the next element of a sequence by default. If prev is True
    it computes the previous element instead."""
    if isinstance(seq, list):
        # numpy arrays allow for better element wise operations
        seq = np.array(seq)
    sub_seq = seq[1:] - seq[:-1]
    if any(sub_seq):
        if prev:
            return seq[0] - find_val(sub_seq, prev=True)
        else:
            return find_val(sub_seq) + seq[-1]
    else:
        return seq[0] if prev else seq[-1]


print(f"Part 1 Solution: {sum([find_val(h) for h in histories])}")
print(f"Part 2 Solution: {sum([find_val(h, prev=True) for h in histories])}")
