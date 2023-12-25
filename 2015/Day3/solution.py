"""Advent of Code 2015 Day 3 Solution
Completion Date: 04/12/2023"""

from typing import Dict, List, Tuple

with open("input_test.txt") as f:
    instruct: str = f.read()

# Mapping of the instruction symbols to a representation of
# the direction of motion in a 2D plane
dirs: Dict[str, Tuple[int, int]] = {
    "^": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, -1),
}


def get_coors(instructions: str) -> List[Tuple[int, int]]:
    """This function returns all coordinates visited from a set of
    instructions provided"""

    coors_visited: List[Tuple[int, int]] = []
    coor: Tuple[int, int] = (0, 0)

    for i in instructions:
        if coor not in coors_visited:
            coors_visited.append(coor)
        coor = (coor[0] + dirs[i][0], coor[1] + dirs[i][1])
    return coors_visited


print(f"Part 1 Solution: {len(get_coors(instruct))}")
print(f"Part 2 Solution: {len(set(get_coors(instruct[::2]) + get_coors(instruct[1::2])))}")
