"""Advent of Code 2015 Day 6 Solution"""

import re
from typing import List, Tuple
import numpy as np

with open("input_test.txt") as f:
    instruct: List[str] = [line.strip() for line in f.readlines()]

light_grid: np.ndarray = np.zeros((1000, 1000))  # whether light is on (1) or off (0)
brightness: np.ndarray = np.zeros((1000, 1000))  # brightness of the light

for i in instruct:
    coors: List[int] = [int(j) for j in re.findall(r"\d+", i)]
    x: Tuple[int, int] = (coors[0], coors[2] + 1)  # x range to modify
    y: Tuple[int, int] = (coors[1], coors[3] + 1)  # y range to modify

    # shape of rectangle to modify
    rect_shape: Tuple[int, int] = (x[1] - x[0], y[1] - y[0])
    ones: np.ndarray = np.ones(rect_shape)  # array of ones of appropriate shape

    if i.startswith("turn on "):
        light_grid[x[0] : x[1], y[0] : y[1]] = ones
        brightness[x[0] : x[1], y[0] : y[1]] += ones
    elif i.startswith("turn off "):
        light_grid[x[0] : x[1], y[0] : y[1]] = np.zeros(rect_shape)
        brightness[x[0] : x[1], y[0] : y[1]] -= ones
        brightness[brightness < 0] = 0  # brightness cannot be negative
    else:  # assumes instruction is 'toggle'
        light_grid[x[0] : x[1], y[0] : y[1]] = 1 - light_grid[x[0] : x[1], y[0] : y[1]]
        brightness[x[0] : x[1], y[0] : y[1]] += 2 * ones

print(f"Part 1 Solution : {int(np.sum(light_grid))}")
print(f"Part 2 Solution : {int(np.sum(brightness))}")
