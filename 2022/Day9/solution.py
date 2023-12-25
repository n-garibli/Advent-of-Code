"""Advent of Code 2022 Day 9 Solution
Fully rewrote my 2022 solution on 25/12/2023"""

from typing import List, Dict, Tuple

with open("input_test.txt") as f:
    movements: List[str] = f.read().splitlines()

# Stores tuples representing directions of motion for each instruction
Ds: Dict[str, Tuple[int, int]] = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def evolve_tail(t_coor: Tuple[int, int], h_coor: Tuple[int, int]) -> Tuple[int, int]:
    """Given the coordinate of the head (h_coor), and the coordinate of the tail
    this function outputs the new coordinate of the tail as it tries to keep up with
    the head for a rope of length 1."""
    diff = (h_coor[0] - t_coor[0], h_coor[1] - t_coor[1])
    if not any(abs(x) > 1 for x in diff):  # head is touching tail, no need to move
        return t_coor

    distance = sum(abs(x) for x in diff)  # manhattan distance
    d1 = 1 if diff[0] > 0 else -1  # direction to move tail in dim 0
    d2 = 1 if diff[1] > 0 else -1  # direction to move tail in dim 1

    if distance > 2:  # must move diagonally
        t_coor = t_coor[0] + d1, t_coor[1] + d2
    elif abs(diff[0]) > 1:
        t_coor = (t_coor[0] + d1, t_coor[1])
    elif abs(diff[1]) > 1:
        t_coor = (t_coor[0], t_coor[1] + d2)

    return t_coor


h_coor: Tuple[int, int] = (0, 0)
t_coor: Tuple[int, int] = (0, 0)
t_coors: List[Tuple[int, int]] = [(0, 0)]

for i in movements:
    d: Tuple[int, int] = Ds[i[0]]
    for _ in range(int(i.split(" ")[-1])):
        h_coor = (h_coor[0] + d[0], h_coor[1] + d[1])
        t_coor = evolve_tail(t_coor, h_coor)
        t_coors.append(t_coor)

print(f"Part 1 Solution: {len(set(t_coors))}")

for _ in range(8):
    t_coor = (0, 0)
    # treat the positions of the previous knot as a head and evolve the
    # next knot accordingly. Do this 8 times as we are starting from the
    # positions of the first knot (after the head)
    for i, head_coor in enumerate(t_coors):
        t_coor = evolve_tail(t_coor, head_coor)
        t_coors[i] = t_coor

print(f"Part 2 Solution: {len(set(t_coors))}")
