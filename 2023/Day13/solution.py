"""Advent of Code 2023 Day 13 Solution"""

from typing import List, Tuple, Optional, Union
import numpy as np

with open("input.txt") as f:
    ground: List[str] = f.read().split("\n\n")


def find_reflection_axis(
    grid: np.ndarray,
    axis: int,
    smudge_search: bool = False,
    invalid_i: Optional[int] = None,
) -> Union[int, Tuple[int, int]]:
    """Given a binary grid this function will find the index of the axis of
    reflection along the axis specified (0 for rows, 1 for columns). Returns
    None if no valid axes are found. Otherwise it will return the integer index
    of the last row/column before the axis. invalid_i is an optional index to
    not consider as an axis for reflection. If smudge search is specified,
    the function will instead return the coordinate of the point that must
    be changed in order to obtain a different valid reflection axis."""

    d: int = len(grid[0]) if axis else len(grid)
    g: np.array = grid.transpose() if axis else grid

    for j in range(d - 1):
        if invalid_i == j:  # Don't look for a reflection along this axis
            continue
        # Defining the two arrays that must be equal for reflection
        # axis to be right below j
        if 2 * (j + 1) <= d:
            arr1 = g[: j + 1]
            arr1_start = 0
            arr2 = np.flip(g[j + 1 : 2 * (j + 1)], axis=0)
        else:
            arr1 = g[2 * (j + 1) - d : j + 1]
            arr1_start = 2 * (j + 1) - d
            arr2 = np.flip(g[j + 1 :], axis=0)

        if smudge_search:
            diff = arr1 - arr2
            if abs(np.sum(diff)) == 1 and len(np.where(diff != 0)[0]) == 1:
                # These two conditions define where a smudge could be
                smudge_loc = np.where(diff != 0)
                return (arr1_start + smudge_loc[0][0], smudge_loc[1][0])
        elif np.array_equal(arr1, arr2):  # Found the mirror
            return j

    return None


def find_reflection(
    grid: np.ndarray, invalid_i: Tuple[Optional[int], Optional[int]] = (None, None)
) -> Tuple[Optional[int], Optional[int]]:
    """Will look for an axis of reflection in both the rows and the columns.
    Will return a tuple containing the index just before the axis where a
    reflection was found for rows and columns (one of them will be None as
    there is only one mirror in the grid)"""
    i = find_reflection_axis(grid, 0, invalid_i=invalid_i[0])
    if i is not None:
        # No need to look for reflection in columns since found one in rows
        return (i, None)
    j = find_reflection_axis(grid, 1, invalid_i=invalid_i[1])
    return (i, j)


def fix_smudge(grid: np.ndarray, old_ref: Tuple[Optional[int], Optional[int]]):
    """Given the original reflection axis (old_ref) this function finds
    the smudge, removes it and returns an tuple defining the new reflection axis"""
    x_smudge = find_reflection_axis(grid, 0, smudge_search=True)
    if x_smudge is not None:
        grid[x_smudge[0], x_smudge[1]] = not grid[x_smudge[0], x_smudge[1]]
        new_ref = find_reflection(grid, invalid_i=old_ref)
    else:
        y_smudge = find_reflection_axis(grid, 1, smudge_search=True)
        grid[y_smudge[1], y_smudge[0]] = not grid[y_smudge[1], y_smudge[0]]
        new_ref = find_reflection(grid, invalid_i=old_ref)

    return (new_ref[x] if new_ref[x] != old_ref[x] else None for x in range(2))


total_p1 = 0
total_p2 = 0
for k, i in enumerate(ground):
    i = i.splitlines()
    # Creating a np array for each grid in the input
    grid: np.array = np.zeros((len(i), len(i[0])))
    for j, val in enumerate(i):
        grid[j] = np.array(list(val)) == "#"

    r, c = find_reflection(grid)
    total_p1 += 100 * (r + 1) if r is not None else (c + 1)

    r2, c2 = fix_smudge(grid, old_ref=(r, c))
    total_p2 += 100 * (r2 + 1) if r2 is not None else (c2 + 1)


print(f"Part 1 Solution: {total_p1}")
print(f"Part 2 Solution: {total_p2}")
