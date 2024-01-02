"""Advent of Code 2015 Day 25 Part 1 Solution
Completed on 02/01/2024. Brute force at the minute (7s)"""

from typing import Tuple

n: int = 27995004  # starting number
pos: Tuple[int, int] = (6, 6)  # starting position


def get_next_num(prev_num: int, prev_pos: Tuple[int, int]) -> (int, Tuple[int, int]):
    """This function gets the next number in the sequence
    and its position on the infinite piece of paper."""
    new_num = (prev_num * 252533) % 33554393
    new_pos = (prev_pos[0] - 1, prev_pos[1] + 1)
    if new_pos[0] == 0:
        new_pos = (prev_pos[1] + 1, 1)
    return new_num, new_pos


# my puzzle input
target_pos: Tuple[int, int] = (2978, 3083)

while pos != target_pos:
    n, pos = get_next_num(n, pos)

print(f"Part 1 Solution: {n}")
