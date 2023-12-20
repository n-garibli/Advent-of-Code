"""Advent of Code 2022 Day 2 Solution"""

from typing import List, Dict

with open("input_test.txt") as f:
    rounds: List[str] = f.read().splitlines()

# Stores the points that a move is worth (X,Y,Z only applicable for part 1 )
points: Dict[str, int] = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def get_round_score(my_points: int, opponent_points: int) -> int:
    """Calculates my score for a game given the points that my move
    and my opponents move is worth"""
    score = my_points
    if my_points == opponent_points:  # our moves are the same
        score += 3
    elif (my_points, opponent_points) in [(1, 3), (3, 1)]:
        # To ensure that rock beats scissors
        score += 6 * (my_points == 1)
    else:
        score += 6 * (my_points > opponent_points)
    return score


print(f"Part 1 Solution: {sum([get_round_score(points[r[-1]],points[r[0]]) for r in rounds])}")

total_score: int = 0
for r in rounds:
    opponent_points: int = points[r[0]]
    if r[-1] == "Y": # draw
        my_points = opponent_points
    elif r[-1] == "Z": # I win
        my_points = 1 if opponent_points == 3 else opponent_points + 1
    else: # I lose
        my_points = 3 if opponent_points == 1 else opponent_points - 1

    total_score += get_round_score(my_points, opponent_points)

print(f"Part 2 Solution: {total_score}")
