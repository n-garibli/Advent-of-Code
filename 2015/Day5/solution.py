"""Advent of Code 2015 Day 5 Solution"""

import re
from typing import List

with open("input_test.txt") as f:
    strings: List[str] = [line.strip() for line in f.readlines()]

n_nice_strings: int = 0
for s in strings:
    if len(re.findall(r"[aeiou]", s)) < 3:
        continue  # ensures at least 3 vowels
    if any([x in s for x in ["ab", "cd", "pq", "xy"]]):
        continue  # ensures no forbidden substrings
    # check that a letter repeats
    for letter in s:
        if letter + letter in s:
            n_nice_strings += 1
            break

print(f"Part 1 Solution: {n_nice_strings}")

n_nice_strings: int = 0
for s in strings:
    cond_1: bool = False  # contains non overlapping repeating letters
    cond_2: bool = False  # contains a letter which repeats with a letter between

    # iterating through the letters in the string
    for i in range(len(s) - 2):
        if s[i] + s[i + 1] in s[i + 2 :] and not cond_1:
            cond_1 = True
        if s[i] == s[i + 2] and not cond_2:
            cond_2 = True
        if cond_1 and cond_2:
            n_nice_strings += 1
            break

print(f"Part 2 Solution: {n_nice_strings}")
