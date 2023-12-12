"""Advent of Code 2023 Day 11 Solution"""

from typing import List, Tuple
import numpy as np

with open("input.txt") as f:
    sky: List[str] = f.read().splitlines()

# These will store the ids of all rows and columns that expanded
exp_r: List[int] = []
exp_c: List[int] = []

# populating a numpy array that will contain the sky image
dim_r: int = len(sky)
dim_c: int = len(sky[0])
sky_grid: np.array = np.zeros((dim_r, dim_c))

for i in range(dim_r):
    sky_grid[i] = np.array(list(sky[i])) == "#"
    if not any(sky_grid[i]):
        exp_r.append(i)
for j in range(dim_c):
    if not any(sky_grid[:, j]):
        exp_c.append(j)

# Storing these as numpy arrays for ease of use later
exp_r: np.array = np.array(exp_r)
exp_c: np.array = np.array(exp_c)

# Extracting the coordinates of all the galaxies
xs, ys = np.where(sky_grid == 1)
galaxy_coors: List[Tuple[int, int]] = [(x, y) for x, y in zip(xs, ys)]


def distance(coor1: Tuple[int, int], coor2: Tuple[int, int], expansion: int) -> int:
    """Finds distance between two points given an expansion factor
    of the universe"""

    # traditional manhattan distance between two coordinates
    manhattan = abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])

    # additional distance travelled due to traversing columns/rows that expanded
    additional_dist = 0
    if coor1[0] > coor2[0]:
        additional_dist += (expansion - 1) * np.logical_and(
            exp_r > coor2[0], exp_r < coor1[0]
        ).sum()
    else:
        additional_dist += (expansion - 1) * np.logical_and(
            exp_r > coor1[0], exp_r < coor2[0]
        ).sum()

    if coor1[1] > coor2[1]:
        additional_dist += (expansion - 1) * np.logical_and(
            exp_c > coor2[1], exp_c < coor1[1]
        ).sum()
    else:
        additional_dist += (expansion - 1) * np.logical_and(
            exp_c > coor1[1], exp_c < coor2[1]
        ).sum()

    return manhattan + additional_dist


def find_total_distance(coors: List[Tuple[int, int]], expansion: int) -> int:
    """Finds the sum of the shortest paths between all pairs of coors in the
    input list"""
    tot_distance = 0
    for i, coor1 in enumerate(coors):
        for j, coor2 in enumerate(coors[i + 1 :]):
            tot_distance += distance(coor1, coor2, expansion=expansion)
    return tot_distance


print(f"Part 1 Solution: {find_total_distance(galaxy_coors, expansion=2)}")
print(f"Part 2 Solution: {find_total_distance(galaxy_coors, expansion=1000000)}")
