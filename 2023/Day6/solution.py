"""Advent of Code 2023 Day 6 Solution"""

import re
import numpy as np  # using numpy is much faster than iterating over all possible speeds

with open("input_test.txt") as f:
    times, records = [re.findall(r"\d+", line) for line in f.readlines()]


def find_n_ways(time, record):
    """This function returns the number of ways in which a record can be beaten given
    the duration of the race"""
    speeds = np.arange(0, time)
    distances = (time - speeds) * speeds
    return np.sum(distances > record)


print(f"Part 1 Solution : {np.prod([find_n_ways(int(t),int(r)) for t,r in zip(times,records)])}")
print(f"Part 2 Solution : {find_n_ways(int(''.join(times)), int(''.join(records)))}")
