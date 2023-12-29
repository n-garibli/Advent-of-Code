"""Advent of Code 2015 Day 16 Solution
Completed on 11/01/2023, reformatted on 29/12/2023."""

from typing import List, Set, Dict

ticker: Dict[str, int] = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

with open("input.txt") as f:
    sues: List[str] = f.read().splitlines()

# for part 2 special1 are the categories where value needs to be smaller than whats on
# the ticker and special2 are categories where value needs to be greater than whats on
# the ticker. normal contains values that must be exactly as in the ticker
special1: Set[str] = {"pomeranians", "goldfish"}
special2: Set[str] = {"cats", "trees"}
normal: Set[str] = set(ticker.keys()) - special1 - special2

for i, sue in enumerate(sues):
    if all(c + ": " + str(val) in sue for c, val in ticker.items() if c in sue):
        print(f"Part 1 Solution: {i+1}")

    if (
        all(
            int(sue.split(c + ": ")[1].split(",")[0]) < ticker[c]
            for c in special1
            if c in sue
        )
        and all(
            int(sue.split(c + ": ")[1].split(",")[0]) > ticker[c]
            for c in special2
            if c in sue
        )
        and all(c + ": " + str(ticker[c]) in sue for c in normal if c in sue)
    ):
        print(f"Part 2 Solution: {i+1}")
