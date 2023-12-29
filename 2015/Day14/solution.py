"""Advent of Code 2015 Day 14 Solution
Completed on 11/01/2023, rewritten on 29/12/2023"""

import re
import numpy as np

with open("input.txt") as f:
    reindeer_info = [map(int, re.findall(r"\d+", x)) for x in f.readlines()]


def get_km_travelled(speed: int, fly_time: int, rest_time: int, race: int) -> int:
    """This function outputs the distance travelled by a raindeer (in km) during a race
    of duration 'race' seconds given that the reindeer flies for 'fly_time' seconds at 
    speed 'speed' and then rests for 'rest_time' seconds."""
    distance = speed * fly_time * (race // (rest_time + fly_time))
    if race % (rest_time + fly_time) <= fly_time:
        return distance + speed * (race % (rest_time + fly_time))
    return distance + speed * fly_time


# This 2D array will store the distance traveled by each reindeer (rows) at each time point (cols)
full_results: np.array = np.zeros((len(reindeer_info), 2503))
times = np.arange(1, 2504)
get_km_travelled = np.vectorize(get_km_travelled)

for i, reindeer in enumerate(reindeer_info):
    speed, moving_time, rest_time = reindeer
    full_results[i] = get_km_travelled(speed, moving_time, rest_time, times)

# maximum value in the last column is the max distance travelled by any reindeer
print(f"Part 1 Solution: {int(np.max(full_results[:,-1]))}")

# create boolean array containing True if a reindeer had the max value at that time point
points_awardered = full_results == np.max(full_results, axis=0)
print(f"Part 2 Solution: {max(np.sum(points_awardered,axis=1))}")
