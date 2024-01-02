"""Advent of Code 2015 Day 19 Solution
Part 1 completed on 02/01/2024. Part 2 is stupid
so I'm not gonna do it yet."""

from typing import List, Set
import re

with open("input.txt") as f:
    replacements, molecule = f.read().split("\n\n")
    replacements: List[str] = replacements.splitlines()


def replace1(mol: str, instructions: List[str]) -> Set[str]:
    """Returns a set of new molecules that can be created with 1 replacement"""
    new_mols = set()
    for inst in instructions:
        original, replacement = inst.split(" => ")
        for x in re.finditer(original, mol):
            new_mol = mol[: x.start()] + replacement + mol[x.end() :]
            new_mols.add(new_mol)
    return new_mols


print(f"Part 1 Solution: {len(replace1(molecule,replacements))}")

# I tried BFS and DFS for Part 2 but they fail (take unreasonably long)...
# After browsing reddit, turns out there are quirks in the input that need
# to be used (ie its not reasonable to come up with a general solution,
# hence I don't like this puzzle and I'm going to abandon this for now)
