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


def tilt_north(rock_grid: np.array) -> np.array:
    """Alters the input array as if performing a tilt to the north, so that
    all the round rocks (O) go to the top"""

    for i in range(d):
        # This is a list of Os in column i split by the # between them
        # Eg: ["","OOOO",""] implies that between the first 2 # there are 4 Os
        O: List[str] = "".join(rock_grid[:, i][rock_grid[:, i] != "."]).split("#")
        # remove all Os from column i (to be put in a new place later)
        rock_grid[:, i][rock_grid[:, i] == "O"] = "."
        if "O" in O[0]:
            # means there were Os before the first #, putting them all at the top
            rock_grid[:, i][: len(O[0])] = "O"

        for j, k in enumerate(np.where(rock_grid[:, i] == "#")[0]):
            # putting all the Os that come after a particular # right after it
            if O[j + 1] != "":
                rock_grid[:, i][k + 1 : k + 1 + len(O[j + 1])] = "O"

    return rock_grid


def get_north_load(grid: np.array) -> int:
    """Computes north load given arrangement of rocks"""
    return sum([np.sum(grid[i] == "O") * (d - i) for i in range(d)])


def cycle(rock_grid: np.array) -> np.array:
    """This function completes one cycle of tilting the rocks in every
    direction"""
    for _ in range(4):
        rock_grid = np.rot90(tilt_north(rock_grid), k=-1)
    return rock_grid


print(f"Part 1 Solution: {get_north_load((tilt_north(rock_grid)))}")

# rock_grid has mutated whilst solving part 1 so resetting it
rock_grid = original_rock_grid

# using the tobytes() method to make a np array hashable
cache = [rock_grid.tobytes()]  # stores previously seen rock arrangements
# stores north loads for all previously seen rock arrangements
cache_vals = {rock_grid.tobytes(): get_north_load(rock_grid)}


# This loop search for an inevitable cycle in the rock movements
# by checking if an arrangement of rocks has previously been seen
while True:
    rock_grid = cycle(rock_grid)
    h = rock_grid.tobytes()
    cache_vals[h] = get_north_load(rock_grid)
    if h in cache:
        start = cache.index(h)
        # calculating the length of the cycle
        cycle_l = len(cache) - start
        break
    else:
        cache.append(h)

# The arrangement after 1000000000 cycles will be the same as after 
# (1000000000 - start) % cycle_l + start based on the cycle length and 
# where the cycle begins
print(f"Part 2 Solution: {cache_vals[cache[(1000000000 - start) % cycle_l + start]]}")
