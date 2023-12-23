"""Advent of Code 2022 Day 10 Solution"""

from typing import List

with open("input_test.txt") as f:
    instructions: List[str] = f.read().splitlines()

x: int = 1  # Current CPU signal
i: int = 1  # Cycle
signal_strength: int = 0  # Total signal strength
for val in instructions:
    if i in [20, 60, 100, 140, 180, 220]:
        signal_strength += i * x

    if val == "noop":
        i += 1
    else:
        if i + 1 in [20, 60, 100, 140, 180, 220]:
            signal_strength += (i + 1) * x
        i += 2  # 2 cycles to execute
        x += int(val.split(" ")[-1])

print(f"Part 1 Solution {signal_strength}")
