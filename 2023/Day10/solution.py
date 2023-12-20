"""Advent of Code 2023 Day 10 Solution"""

from typing import List, Tuple, Dict
import numpy as np

with open("input_test.txt") as f:
    pipes: List[str] = f.read().splitlines()

dim_r: int = len(pipes)
dim_c: int = len(pipes[0])
pipe_grid: np.array = np.zeros((dim_r, dim_c), dtype=str)

# populating a numpy array that will contain the pipes as a grid
for i in range(dim_r):
    pipe_grid[i] = np.array(list(pipes[i]))


# This dictionary helps me find the next coordinate for moving
# in a particular direction
Ds: Dict[str, Tuple[int, int]] = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

# This defines which directions are valid directions of motion
# given the shape of a pipe
valid_dirs_given_pipe: Dict[str, List[str]] = {
    "-": ["right", "left"],
    "L": ["up", "right"],
    "J": ["up", "left"],
    "|": ["up", "down"],
    "F": ["down", "right"],
    "7": ["down", "left"],
}


def check_directions(
    c: Tuple[int, int], directions: List[str]
) -> List[Tuple[int, int]]:
    """This function will return a list of valid next coordinates given a list of directions
    to check and the current coordinate c"""
    valid_coors: List[Tuple[int, int]] = []
    for d in directions:
        assert d in Ds.keys(), f"Got invalid direction {d}"
        x, y = (c[0] + Ds[d][0], c[1] + Ds[d][1])
        if x < 0 or x > dim_r - 1 or y < 0 or y > dim_c - 1:
            # coordinate out of bounds
            continue
        elif d == "up" and pipe_grid[x, y] in "|F7":
            valid_coors.append((x, y))
        elif d == "down" and pipe_grid[x, y] in "|JL":
            valid_coors.append((x, y))
        elif d == "right" and pipe_grid[x, y] in "J7-":
            valid_coors.append((x, y))
        elif d == "left" and pipe_grid[x, y] in "LF-":
            valid_coors.append((x, y))
    return valid_coors


def find_next_pipe(path=List[Tuple[int, int]]) -> Tuple[int, int]:
    """This function will return the coordinate of the next element
    given the path that has been followed so far"""
    dirs = valid_dirs_given_pipe[pipe_grid[path[-1]]]
    new_coors = check_directions(path[-1], dirs)

    for new_coor in new_coors:
        # One vaild new coor will involve going back on itself
        if new_coor != path[-2]:
            # pipe_grid[coor[0], coor[1]] = "P"
            return new_coor


start: Tuple[int, int] = tuple([int(x) for x in np.where(pipe_grid == "S")])
# pipe_grid[start[0], start[1]] = "P"
next_coors: List[Tuple[int, int]] = check_directions(
    start, ["up", "down", "left", "right"]
)

# initialise 2 paths - one will evolve clockwise, one anticlockwise
path1, path2 = [start, next_coors[0]], [start, next_coors[1]]

# When the two paths reach the same point, that point is the
# furthest from the start
while path1[-1] != path2[-1]:
    path1.append(find_next_pipe(path1))
    path2.append(find_next_pipe(path2))

print(f"Part 1 Solution: {len(path1) - 1}")

# For part 2 I'm planning to change the original path_grid so
# that the path is denoted by P and implement some kind of
# flood filling algorithm (when I have a bit more time)
