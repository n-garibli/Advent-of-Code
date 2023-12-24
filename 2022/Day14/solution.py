"""Advent of Code 2022 Day 14 Solution
Rewritten on 24/12/2023"""

import re
from typing import List, Tuple
import numpy as np


with open("input_test.txt") as f:
    rocks: List[List[str]] = [x.split(" -> ") for x in f.read().splitlines()]

# Extracting the coordinates of all rocks from the input
all_coors = []
for rock_path in rocks:
    x, y = tuple(map(int, re.findall("\d+", rock_path[0])))
    for i, coor in enumerate(rock_path[:-1]):
        x2, y2 = tuple(map(int, re.findall("\d+", rock_path[i + 1])))
        if x2 > x:
            new_coors = [(j, y) for j in range(x, x2 + 1)]
        elif x2 < x:
            new_coors = [(j, y) for j in range(x2, x + 1)]
        elif y2 > y:
            new_coors = [(x, j) for j in range(y, y2 + 1)]
        elif y2 < y:
            new_coors = [(x, j) for j in range(y2, y + 1)]
        all_coors.extend(new_coors)
        x, y = x2, y2


all_coors = np.array(all_coors)
x_min = all_coors[:, 0].min()
all_coors[:, 0] = all_coors[:, 0] - x_min
# Constructing a numpy array with rocks as 1 and empty space as 0
# In this array all coordinates from the original input must be shifted
# by x_min for indexing
rock_grid = np.zeros((all_coors[:, 1].max() + 1, all_coors[:, 0].max() + 1))
rock_grid[all_coors[:, 1], all_coors[:, 0]] = 1


def drop_one_grain(rock_grid: np.array, sand_start: Tuple[int, int]) -> Tuple[int, int]:
    """This function finds the coordinates of a grain of sand dropped at coordinate
    sand_start after it has come to rest, given a numpy array of the rock positions"""

    y, x = sand_start
    while rock_grid[y + 1, x] < 1:  # keep moving down whilst possible
        if y != rock_grid.shape[0] - 2:
            y += 1
        else:
            return None

    if x - 1 < 0:  # falling into abyss from the left
        return None
    elif rock_grid[y + 1, x - 1]:  # cannot go left
        if x + 1 > rock_grid.shape[1] - 1:  # falling into abyss from the right
            return None
        elif rock_grid[y + 1, x + 1]:  # cannot go right
            return (y, x)
        else:  # go as far diagonally right as possible
            return drop_one_grain(rock_grid, (y + 1, x + 1))
    else:  # go as far diagonally left as possible
        return drop_one_grain(rock_grid, (y + 1, x - 1))


def drop_sand(rock_grid: np.array, sand_start_x: int, floor=False) -> np.array:
    """This function drops sand from the top at coordinate sand_start_x in a
    given rock grid until sand starts flowing into the abyss below (if floor is false)
    or if the starting point gets blocked. The rock grid is modified to contain 2s
    where the sand grains are."""
    if floor:  # adding a floor of rocks at the bottom of the grid
        x_max = rock_grid.shape[1]
        rock_grid = np.concatenate(
            [rock_grid, np.full((1, x_max), 0), np.full((1, x_max), 1)]
        )

    new_grain_coor = drop_one_grain(rock_grid, (0, sand_start_x))
    while new_grain_coor is not None:
        rock_grid[new_grain_coor] = 2
        new_grain_coor = drop_one_grain(rock_grid, (0, sand_start_x))

        if floor:
            while new_grain_coor is None:
                # add additional columns on each side with the floor so that the
                # sand doesn't fall into the abyss
                new_col = np.array([[0] * (rock_grid.shape[0] - 1) + [1]]).transpose()
                rock_grid = np.concatenate([new_col, rock_grid, new_col], axis=1)
                sand_start_x += 1  # position moved in rock_grid coordinates due to additional column
                new_grain_coor = drop_one_grain(rock_grid, (0, sand_start_x))

        if rock_grid[0, sand_start_x] == 2:  # blocked starting point
            break
    return rock_grid


new_grid = drop_sand(rock_grid, 500 - x_min, floor=False)
print(f"Part 1 Solution: {(np.sum(new_grid) - np.sum(new_grid[new_grid==1]))/2}")

# can just start from the grid obtained from part 1 as the sand will evolve in the
# same way up until that point
new_grid = drop_sand(new_grid, 500 - x_min, floor=True)
print(f"Part 2 Solution: {(np.sum(new_grid) - np.sum(new_grid[new_grid==1]))/2}")
