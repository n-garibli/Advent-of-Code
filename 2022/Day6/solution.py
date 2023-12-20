"""Advent of Code 2022 Day 6 Solution"""

signal: str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def marker_id(signal: str, n_unique: int):
    """Returns the first index where the preceding n_unique elements
    of signal are different from eachother"""
    for i in range(n_unique, len(signal)):
        if len(set(signal[i - n_unique : i])) == n_unique:
            return i


print(f"Part 1 Solution: {marker_id(signal, 4)}")
print(f"Part 2 Solution: {marker_id(signal, 14)}")
