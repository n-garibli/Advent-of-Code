"""Advent of Code 2023 Day 2 Solution"""

# Imports
from typing import List, Dict
import re

# Load input
with open("input_test.txt") as f:
    games: List[str] = [line.strip() for line in f.readlines()]

# Specifying the maximum number of each colour of cubes
# as said in the problem for part 1
max_cubes: Dict[str, int] = {"r": 12, "g": 13, "b": 14}

# this will be updated as part of part 2
game_powers = []

# This is the sum of the ids for all possible games
sum_game_ids: int = 0
for game in games:
    game_id: int = int(game.split(":")[0][5:])

    # minimum number of cubes for this games to be possible
    min_cubes: Dict[str, int] = {"r": 0, "g": 0, "b": 0}

    # whether this game is impossible according to part 1 conditions
    impossible: bool = False

    # Extracting per round information
    rounds: List[str] = game.split(":")[1].split(";")
    for r in rounds:
        for c in ["r", "b", "g"]:
            matches = re.search(f"\d+ {c}", r)
            if matches is not None:
                n_cubes = int(matches.group()[:-1])
                if n_cubes > min_cubes[c]:
                    min_cubes[c] = n_cubes
            else:
                n_cubes = 0
                
            if n_cubes > max_cubes[c]:
                impossible = True
    game_power = min_cubes["r"] * min_cubes["b"] * min_cubes["g"]
    game_powers.append(game_power)

    if not impossible:
        sum_game_ids += game_id

print(f"Part 1 Solution: {sum_game_ids}")
print(f"Part 2 Solution: {sum(game_powers)}")
