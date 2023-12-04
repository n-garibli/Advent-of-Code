# %% --------------------------------------------------------------------------
# {Enter description for cell}
# -----------------------------------------------------------------------------
from typing import Dict, List, Tuple
import numpy as np

with open("input.txt") as f:
    instructions: str = f.read()

# Mapping of the instruction symbols to a representation of
# the direction of motion in a 2D plane
directions: Dict[str, np.array] = {
    "^": np.array([0, 1]),
    ">": np.array([1, 0]),
    "<": np.array([-1, 0]),
    "v": np.array([0, -1]),
}


def get_coors(instructions: str) -> List[Tuple[int, int]]:
    """This function will return all coordinates visited from a set of
    instructions provided"""

    coors_visited: List[Tuple[int, int]] = []

    # Using numpy arrays to store coordinates as they are mutable and
    # support easy elementwise addition
    coor: np.array = np.array([0, 0])
    for i in instructions:
        if tuple(coor) not in coors_visited:
            coors_visited.append(tuple(coor))
        coor += directions[i]
    return coors_visited


# Extracting instructions meant for santa and for robo santa for part 2
for_santa: str = instructions[0::2]
for_robo_santa: str = instructions[1::2]

print(f"Part 1 Solution: {len(get_coors(instructions))}")
print(f"Part 2 Solution: {len(set(get_coors(for_santa) + get_coors(for_robo_santa)))}")
