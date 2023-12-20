"""Advent of Code 2015 Day 1 Solution"""

from typing import Optional

with open("input_test.txt") as f:
    parentheses = f.read()

floor: int = 0

# id of character when basement floor is first accessed
basement_idx: Optional[int] = None  
for i, bracket in enumerate(parentheses):
    if bracket == "(":
        floor += 1
    elif bracket == ")":
        floor -= 1
        
    if floor == -1 and basement_idx is None:
        basement_idx = i + 1

print(f"Part 1 Solution: {floor}")
print(f"Part 2 Solution: {basement_idx}")
