"""Advent of Code 2015 Day 1 Solution"""

with open("input.txt") as f:
    parentheses = f.read()

floor = 0
basement_idx = None
for i, bracket in enumerate(parentheses):
    if bracket == "(":
        floor += 1
    elif bracket == ")":
        floor -= 1
    if floor == -1 and basement_idx is None:
        basement_idx = i + 1

print(f"Part 1 Solution: {floor}")
print(f"Part 2 Solution: {basement_idx}")
