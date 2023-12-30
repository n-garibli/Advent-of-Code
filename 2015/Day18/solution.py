"""Advent of Code 2015 Day 18 Solution
Completed on 18/01/2023 (see old_solution.py), rewritten on 30/12/2023 
for an over 20x speed optimisation by using numpy operations"""

from typing import List, Callable
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as sw_view

with open("input.txt") as f:
    lights: List[str] = f.read().splitlines()

# populating a numpy array that will contain all the status
# of all lights (true for on false for off)
d: int = len(lights)
light_grid: np.ndarray = np.zeros((d, d), dtype=bool)
for i in range(d):
    light_grid[i] = np.array(list(lights[i])) == "#"


def get_n_neighbours(a: np.ndarray) -> np.ndarray:
    """This function returns a numpy array of the same shape as the original array
    but each element is the sum of the surrounding elements of that position
    in the origial array (diagonals included)."""
    n_neighbours: np.ndarray = np.zeros(a.shape, dtype=int)

    # Sum the 3x3 window with every element at the center for all non-boundary elements
    # of the input array
    n_neighbours[1:-1, 1:-1] = np.sum(sw_view(a, (3, 3)), axis=(-1, -2))
    # Considering the edge cases for the outermost top, bottom, left and right line
    # respectively (since in those cases the window of neighbours is of shape 2x3
    # or 3x2)
    n_neighbours[0:1, 1:-1] = np.sum(sw_view(a[[0, 1], :], (2, 3)), axis=(-1, -2))
    n_neighbours[[-1], 1:-1] = np.sum(sw_view(a[[-2, -1], :], (2, 3)), axis=(-1, -2))
    n_neighbours[1:-1, 0:1] = np.sum(sw_view(a[:, [0, 1]], (3, 2)), axis=(-1, -2))
    n_neighbours[1:-1, [-1]] = np.sum(sw_view(a[:, [-2, -1]], (3, 2)), axis=(-1, -2))
    # subtracting the value in the original array since the element is not its own neighbour
    n_neighbours = n_neighbours - a
    # manually populating each corner as they only have 3 neighbours each
    n_neighbours[0, 0] = sum([a[0, 1], a[1, 1], a[1, 0]])
    n_neighbours[0, -1] = sum([a[0, -2], a[1, -2], a[1, -1]])
    n_neighbours[-1, 0] = sum([a[-2, 0], a[-2, 1], a[-1, 1]])
    n_neighbours[-1, -1] = sum([a[-2, -2], a[-1, -2], a[-2, -1]])
    return n_neighbours


def update_light(n_on_neighbours: int, on: bool) -> bool:
    """Given the number of neighbours that are on and whether
    the light is on this function returns True if the light
    should remain on and false otherwise."""
    if on:
        return n_on_neighbours in [2, 3]
    return n_on_neighbours == 3


update_lights: Callable = np.vectorize(update_light)


def take_n_steps(
    lights: np.ndarray,
    n_steps: int,
    fixed_corners: bool = False,
) -> np.ndarray:
    """Evolves the input light grid as per the conway game of life
    n_steps times. If fixed corners is set to true, the corner elements
    are set to 1/True at every step."""
    for _ in range(n_steps):
        n_neighbours = get_n_neighbours(lights)
        lights = update_lights(n_neighbours, lights)
        if fixed_corners:  # set all corner elements to 1
            lights[[0, 0, -1, -1], [0, -1, 0, -1]] = True
    return lights


print(f"Part 1 Solution: {np.sum(take_n_steps(light_grid,100))}")

light_grid[[0, 0, -1, -1], [0, -1, 0, -1]] = 1  # set all corner elements to 1
print(f"Part 2 Solution: {np.sum(take_n_steps(light_grid,100,fixed_corners=True))}")
