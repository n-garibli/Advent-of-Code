"""Advent of Code 2015 Day 21 Solution
Completed on 31/12/2023. Brute force for testing all
possible combinations of purchases is okay since play_game() 
is fast."""

from typing import Dict, List
from math import ceil

# Summary of the shop itinerary. "c" stands for cost,
# "d" stands for damage and "a" stands for armor
weapons: List[Dict[str, int]] = [
    {"c": 8, "d": 4},
    {"c": 10, "d": 5},
    {"c": 25, "d": 6},
    {"c": 40, "d": 7},
    {"c": 74, "d": 8},
]
armors: List[Dict[str, int]] = [
    {"c": 0, "a": 0},  # equivalent to no armor
    {"c": 13, "a": 1},
    {"c": 31, "a": 2},
    {"c": 53, "a": 3},
    {"c": 75, "a": 4},
    {"c": 102, "a": 5},
]

rings: List[Dict[str, int]] = [
    {"c": 0, "d": 0, "a": 0},  # equivalent no ring
    {"c": 25, "d": 1, "a": 0},
    {"c": 50, "d": 2, "a": 0},
    {"c": 100, "d": 3, "a": 0},
    {"c": 20, "d": 0, "a": 1},
    {"c": 40, "d": 0, "a": 2},
    {"c": 80, "d": 0, "a": 3},
]

# my puzzle input
BOSS_STATS: Dict[str, int] = {"hits": 104, "d": 8, "a": 1}


def play_game(stats: Dict[str, int]) -> bool:
    """Returns True if I win and returns False if the boss wins. Makes
    use of arithmetic sequences for quick solution."""
    d = max(1, stats["d"] - BOSS_STATS["a"])  # my damage per round
    d_boss = max(1, BOSS_STATS["d"] - stats["a"])  # boss' damage per round
    n_rounds_to_kill_me = ceil(stats["hits"] / d_boss)
    n_rounds_to_kill_boss = ceil(BOSS_STATS["hits"] / d)
    # I win if it takes the same number of rounds to kill us since I start
    return n_rounds_to_kill_me >= n_rounds_to_kill_boss


min_winning_cost = float("inf")
max_losing_cost = 0
# trying every combination of weapons, armor and rings
for weapon in weapons:
    for armor in armors:
        for i, ring1 in enumerate(rings):  # ring 1
            for j, ring2 in enumerate(rings):  # ring 2
                if i != 0 and i == j:
                    # can't have the same ring on both hands exception is first
                    # element since you CAN have no rings on both hands
                    continue
                my_stats: Dict[str, int] = {
                    "hits": 100,
                    "a": armor["a"] + ring1["a"] + ring2["a"],
                    "d": weapon["d"] + ring1["d"] + ring2["d"],
                }
                total_cost = weapon["c"] + armor["c"] + ring1["c"] + ring2["c"]
                if play_game(my_stats):
                    min_winning_cost = min(min_winning_cost, total_cost)
                else:
                    max_losing_cost = max(max_losing_cost, total_cost)

print(f"Part 1 Solution: {min_winning_cost}")
print(f"Part 2 Solution: {max_losing_cost}")
