"""Advent of Code 2022 Day 12 Solution
Completed in 2022, completely rewritten on 26/12/2023"""

from typing import List, Tuple, Optional, Dict
from string import ascii_lowercase as lc
import numpy as np


with open("input.txt") as f:
    grid: List[str] = f.read().splitlines()

x: int = len(grid)
y: int = len(grid[0])
# populating a numpy array that will represent an elevation map
elevation_map: np.ndarray = np.zeros((x, y), dtype=str)
for i in range(x):
    elevation_map[i] = np.array(list(grid[i]))

# Extract start and target end coordinates from the input
start_coor = tuple(map(int, np.where(elevation_map == "S")))
end_coor = tuple(map(int, np.where(elevation_map == "E")))


def l_to_elevation(l: str) -> int:
    """Transforms a string corresponding to an elevation level
    into an equivalent elevation level as an integer (a is elevation 0
    and z is elevation 25)"""
    if l == "S":
        return 0
    if l == "E":
        return 25
    return lc.index(l)


# elevation map with 0 being lowest elevation and 25 the highest
elevation_map: np.ndarray = np.vectorize(l_to_elevation)(elevation_map)


def find_valid_neighbours(
    coor: Tuple[int, int], e_map: np.ndarray, prev_visited: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """Finds the valid neighbours of a coordinate (coor) given the elevation map (e_map)
    given the constraints that the coordinate must not be in prev_visited and that valid
    neighbours are those that do not increase elevation by more than 1"""
    e = e_map[coor]
    y, x = coor
    valid_neighbours = []
    # condition ensures the corresponding coordinate new_coor is not out of bounds
    for condition, new_coor in zip(
        [y - 1 >= 0, y + 1 < len(e_map), x - 1 >= 0, x + 1 < len(e_map[0])],
        [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)],
    ):
        if condition and (new_coor not in prev_visited) and (e_map[new_coor] - e < 2):
            valid_neighbours.append(new_coor)
    return valid_neighbours


# This acts as a cache for the following function to significantly speed up computation for part 2
coor_min_path: Dict[Tuple[int, int], int] = {}


def get_shortest_pl(
    start: Tuple[int, int],
    end: Tuple[int, int],
    e_map: np.ndarray,
    path_length_break: Optional[int] = None,
) -> int:
    """Implementing bread first search to find the shortest path length from start_coor to end_coor
    without increasing elevation by more than one at every step. The elevation of each coordinate
    is determined by its value in the e_map numpy array. If path_length_break is provided
    the algorithm will return that value if its unable to find a shorter path."""

    prev_visited: List[Tuple[int, int]] = [start]
    neighbours: List[Tuple[int, int]] = find_valid_neighbours(
        start, e_map, prev_visited
    )
    prev_visited.extend(neighbours)
    path_length: int = 0
    while True:
        path_length += 1
        if path_length_break is not None:
            if path_length >= path_length_break:
                # previously found another path that reached endpoint at this length
                # hence current one considered is not the shortest possible
                return path_length

        next_neighbours: List[Tuple[int, int]] = []
        for n in neighbours:
            neighbours_of_n = find_valid_neighbours(n, e_map, prev_visited)
            if n in coor_min_path:
                if coor_min_path[n] < path_length:
                    # previously considered a path where this coordinate was reached
                    # sooner, hence evolving this path further is pointless
                    prev_visited.extend(neighbours_of_n)
                    continue
            coor_min_path[n] = path_length
            next_neighbours.extend(neighbours_of_n)

        if end in next_neighbours:  # found shortest path to the end point
            return path_length + 1

        # will consider next layer neighbours in the next iteration
        neighbours = list(set(next_neighbours))
        prev_visited.extend(neighbours)


shortest_pl = get_shortest_pl(start_coor, end_coor, elevation_map)
print(f"Part 1 Solution: {shortest_pl}")

# These are all the potential starting points for part 2
coors = np.where(elevation_map == 0)
coors: List[Tuple[int, int]] = [
    (int(coors[0][i]), int(coors[1][i])) for i in range(len(coors[0]))
]

for coor in coors: # populate the cache
    # the starting coordinates will be reached at pl = 0 for the path that starts with them
    coor_min_path[coor] = 0

for coor in coors:
    if coor == start_coor:  # this was computed in part 1
        continue
    shortest_pl = min(shortest_pl, get_shortest_pl(coor, end_coor, elevation_map, shortest_pl))

print(f"Part 2 Solution: {shortest_pl}")
