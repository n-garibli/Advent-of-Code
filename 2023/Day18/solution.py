"""Advent of Code 2023 Day 18 Solution"""

from typing import List, Dict, Tuple

with open("input_test.txt") as f:
    instructions: List[str] = f.read().splitlines()

# This dictionary helps me find the next coordinate for moving
# in a particular direction
Ds: Dict[str, Tuple[int, int]] = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def get_area(instructions: List[str], hexadecimal: bool) -> int:
    """This function computes the area of the resulting lava trench
    give the instructions that the elves received. The hexadecimal arg
    determines whether to use hexadecimal distances (as for part 2)"""
    v1: Tuple[int, int] = (0, 0)  # current location
    shoelace: int = 0  # store the output of shoelace formula for all visited vertices
    perimeter: int = 0  # stores the perimeter of the resulting polygon
    for x in instructions:
        # the direction of motion as defined in Ds
        d: Tuple[int, int] = (Ds[["R", "D", "L", "U"][int(x[-2])]] if hexadecimal else Ds[x[0]])

        # the distance travelled
        dist: int = int(x.split("#")[-1][:-2], 16) if hexadecimal else int(x[2:4])

        # new coordinate after moving
        v2 = (v1[0] + d[0] * dist, v1[1] + d[1] * dist)

        # update area and perimeter
        shoelace += v1[0] * v2[1] - v2[0] * v1[1]
        perimeter += dist
        v1 = v2

    # shoelace formula assumes lines of 0 width. Hence, only half of the area of the perimeter
    # boxes lies inside the area computed by the shoelace (so need to add perimeter/2).
    # Adding 1 accounts for the missing area in the corner boxes.
    # Abs() the shoelace output because might be going clockwise instead of anti-clockwise
    return int(abs(shoelace) / 2 + perimeter / 2 + 1)


print(f"Part 1 Solution: {get_area(instructions, hexadecimal=False)}")
print(f"Part 2 Solution: {get_area(instructions, hexadecimal=True)}")
