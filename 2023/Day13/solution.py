"""Advent of Code 2023 Day 13 Solution"""

from typing import List
import numpy as np

with open("input.txt") as f:
    ground: List[str] = f.read().split("\n\n")


def find_reflection(grid: np.ndarray, axis: int):
    """Returns None if no mirrors are found"""
    d: int = len(grid[0]) if axis else len(grid)
    grid = grid.transpose() if axis else grid
    for j in range(d):
        if np.array_equal(grid[j : j + 1], grid[j + 1 : j + 2]):
            if 2 * (j + 1) <= d:
                if np.array_equal(
                    grid[: j + 1], np.flip(grid[j + 1 : 2 * (j + 1)], axis=0)
                ):
                    return j
            else:
                if np.array_equal(
                    grid[2 * (j + 1) - d : j + 1], np.flip(grid[j + 1 :], axis=0)
                ):
                    return j


r = 0
c = 0
for k, i in enumerate(ground):
    i = i.splitlines()

    grid: np.array = np.zeros((len(i), len(i[0])))
    for j,val in enumerate(i):
        grid[j] = np.array(list(val)) == "#"

    j = find_reflection(grid, 0)
    if j is not None:
        r += j + 1
        continue # No need to look for reflection in columns

    j = find_reflection(grid, 1)
    if j is not None:
        c += j + 1
    else:
        print(f"FAILED TO FIND MIRROR, {k}")
        break

print(f"Part 1 Solution: {100 * r + c}")
