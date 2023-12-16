"""Advent of Code 2023 Day 13 Solution"""


from typing import List, Tuple, Optional, Union
import numpy as np
import copy

with open("input.txt") as f:
    ground: List[str] = f.read().split("\n\n")


def find_reflection_axis(
    grid: np.ndarray,
    axis: int,
    smudge_search: bool = False,
    invalid_i=None,
    old_ref=None,
) -> Union[int, Tuple[int, int]]:
    """Returns None if no mirrors are found"""
    d: int = len(grid[0]) if axis else len(grid)
    g = grid.transpose() if axis else grid
    for j in range(d):
        if invalid_i == j:
            # Don't look for a reflection along this axis
            continue
        line1 = g[j : j + 1]
        line2 = g[j + 1 : j + 2]
        if np.array_equal(line1, line2):
            # Defining the two arrays that must be equal for mirror
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
                    smudge_fix_loc = np.where(diff != 0)
                    return (arr1_start + smudge_fix_loc[0][0], smudge_fix_loc[1][0])
            elif np.array_equal(arr1, arr2):
                return j
        elif smudge_search:
            diff = line1 - line2
            if abs(np.sum(diff)) == 1 and len(np.where(diff != 0)[0]) == 1:
                smudge_fix_loc = np.where(diff != 0)
                test_g = copy.copy(g)
                test_g[j, smudge_fix_loc[1][0]] = not test_g[j, smudge_fix_loc[1][0]]
                if (
                    find_reflection_axis(
                        test_g,
                        0,
                        invalid_i=(old_ref[axis] if old_ref is not None else None),
                    )
                    is not None
                ):
                    return (j, smudge_fix_loc[1][0])

    return None


def find_reflection(
    grid: np.ndarray, invalid_i: Tuple[Optional[int], Optional[int]] = (None, None)
) -> Tuple[Optional[int], Optional[int]]:
    i = find_reflection_axis(grid, 0, invalid_i=invalid_i[0])
    if i is not None:
        # No need to look for reflection in columns since found one in rows
        return (i, None)
    j = find_reflection_axis(grid, 1, invalid_i=invalid_i[1])
    return (i, j)


def fix_smudge(grid: np.ndarray, old_ref: Tuple[Optional[int], Optional[int]]):
    
    x_smudge = find_reflection_axis(grid, 0, smudge_search=True, old_ref=old_ref)
    if x_smudge is not None:
        grid[x_smudge[0], x_smudge[1]] = not grid[x_smudge[0], x_smudge[1]]
        new_ref = find_reflection(grid, invalid_i=old_ref)
    else:
        y_smudge = find_reflection_axis(grid, 1, smudge_search=True, old_ref=old_ref)
        grid[y_smudge[1], y_smudge[0]] = not grid[y_smudge[1], y_smudge[0]]
        new_ref = find_reflection(grid, invalid_i=old_ref)
        
    return (new_ref[x] if new_ref[x] != old_ref[x] else None for x in range(2))

r = 0 ; c = 0 ; r2 = 0 ; c2 = 0
for k, i in enumerate(ground):
    i = i.splitlines()

    grid: np.array = np.zeros((len(i), len(i[0])))
    for j, val in enumerate(i):
        grid[j] = np.array(list(val)) == "#"

    j_r, j_c = find_reflection(grid)
    r += j_r + 1 if j_r is not None else 0
    c += j_c + 1 if j_c is not None else 0

    j_r2, j_c2 = fix_smudge(grid, old_ref=(j_r, j_c))
    r2 += j_r2 + 1 if j_r2 is not None else 0
    c2 += j_c2 + 1 if j_c2 is not None else 0

    assert (j_r, j_c) != (j_r2, j_c2)


print(f"Part 1 Solution: {100 * r + c}")
print(f"Part 2 Solution: {100 * r2 + c2}")
