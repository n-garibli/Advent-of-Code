"""Advent of Code 2023 Day 14 Solution"""

from typing import List
import copy
import numpy as np

with open("input.txt") as f:
    rocks: List[str] = f.read().splitlines()

# populating a numpy array that will contain all the rocks
d: int = len(rocks)
rock_grid: np.ndarray = np.zeros((d, d), dtype="str")
for i in range(d):
    rock_grid[i] = np.array(list(rocks[i]))

# storing original arrangement as will need it for pt2
original_rock_grid: np.ndarray = copy.copy(rock_grid)


def tilt(rock_grid: np.ndarray, tilt: str) -> np.array:
    """Mutates input array as if performing tilt"""
    if tilt == "w":
        rock_grid = rock_grid.transpose()
    elif tilt == "e":
        rock_grid = np.flip(rock_grid.transpose(), axis=0)
    elif tilt == "s":
        rock_grid = np.flip(rock_grid, axis=0)
    else:
        assert tilt == "n", f"Got invalid direction {tilt}"

    for i in range(d):
        O: List[str] = "".join(rock_grid[:, i][rock_grid[:, i] != "."]).split("#")
        # remove all Os from collumn so that they can be put in the right
        # place instead
        rock_grid[:, i][rock_grid[:, i] == "O"] = "."
        if "O" in O[0]:
            rock_grid[:, i][: len(O[0])] = "O"

        for j, k in enumerate(np.where(rock_grid[:, i] == "#")[0]):
            if O[j + 1] != "":
                rock_grid[:, i][k + 1 : k + 1 + len(O[j + 1])] = "O"

    # flip array back to normal if not going north
    if tilt == "w":
        rock_grid = rock_grid.transpose()
    elif tilt == "e":
        rock_grid = np.flip(rock_grid, axis=0).transpose()
    elif tilt == "s":
        rock_grid = np.flip(rock_grid, axis=0)
    return rock_grid


def get_north_load(grid: np.ndarray) -> int:
    """Computes north load given arrangement of rocks"""
    return sum([np.sum(grid[i] == "O") * (d - i) for i in range(d)])


print(f"Part 1 Solution: {get_north_load((tilt(rock_grid,'n')))}")

rock_grid = copy.copy(original_rock_grid)

cache_vals = {rock_grid.tobytes(): get_north_load(rock_grid)}
cache = [rock_grid.tobytes()]

while True:
    for direction in "nwse":
        rock_grid = tilt(rock_grid, direction)
    h = rock_grid.tobytes()
    cache_vals[h] = get_north_load(rock_grid)
    if h in cache:
        start = cache.index(h)
        cycle = len(cache) - start
        break
    else:
        cache.append(h)

print(f"Part 2 Solution: {cache_vals[cache[(1000000000 - start) % cycle + start]]}")
