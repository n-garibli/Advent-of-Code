"""Advent of Code 2022 Day 8 Solution"""

import re
from typing import List, Tuple, Union
import numpy as np

with open("input_test.txt") as f:
    grid_rows: List[str] = f.read().splitlines()


dim: int = len(grid_rows)

# Representing the tree grid as a numpy array
tree_map: np.ndarray = np.zeros((dim, dim), dtype=int)
for i, row in enumerate(grid_rows):
    tree_map[i] = np.array(list(map(int, re.findall(r"\d", row))))


def analyse_view_1d(trees_to_check: Union[List, np.array], test_tree: int):
    """Checks whether a test_tree is visible given a list of trees in front of it
    and computes the number of trees that are visible from the position of test_tree"""
    score: int = 0
    visible: bool = True
    for tree in trees_to_check:
        score += 1
        if test_tree <= tree:
            visible = False
            break
    return score, visible


def analyse_view_4d(i: int, j: int) -> Tuple[int, bool]:
    """Computes the scenic score of a tree in position (i,j) and checks
    if it is visible from any direction"""
    test_tree = tree_map[i, j]
    s_l, vis_l = analyse_view_1d(tree_map[i][:j][::-1], test_tree)  # left
    s_r, vis_r = analyse_view_1d(tree_map[i][j + 1 :], test_tree)  # right
    s_u, vis_u = analyse_view_1d(tree_map[:i, j][::-1], test_tree)  # up
    s_d, vis_d = analyse_view_1d(tree_map[i + 1 :, j], test_tree)  # down

    scenic_score: int = s_l * s_r * s_u * s_d
    visible: bool = any([vis_l, vis_r, vis_u, vis_d])

    return scenic_score, visible


interior_visible: int = 0
max_score: int = 0
for i in range(1, dim - 1):  # no need to consider trees on the edges
    for j in range(1, dim - 1):
        score, visible = analyse_view_4d(i, j)
        interior_visible += visible
        max_score = max([score,max_score])

print(f"Part 1 Solution: {interior_visible + 4 * dim - 4}")
print(f"Part 2 Solution: {max_score}")
