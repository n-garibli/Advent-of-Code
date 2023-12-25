"""Advent of Code 2023 Day 19 Solution
Completion date: 25/12/2023"""

from typing import List, Dict, Tuple
import copy
from math import prod

with open("input_test.txt") as f:
    inp = f.read().splitlines()
    split_i = inp.index("")

# Store all the rules as a dictionary with their names as keys
# E.g. : {'in': 's<1351:px,qqz'}
rules: Dict[str, str] = {n: r[:-1] for n, r in [r.split("{") for r in inp[:split_i]]}

# Store the part infos as a list of dictionaries
# E.g. : [{'x' : 1, 'm' : 2, 'a' : 3, 's': 4},....]
parts: List[Dict[str, int]] = []
for p in inp[split_i + 1 :]:
    scores: Dict[str, int] = {
        s1: int(s2) for s1, s2 in [s.split("=") for s in p[1:-1].split(",")]
    }
    parts.append(scores)


def part_accepted(part: Dict[str, int]) -> bool:
    """Determines whether a part is accepted given its scores."""
    outcome = check_rule(part, "in")
    while outcome not in ["R", "A"]:
        outcome = check_rule(part, outcome)
    if outcome == "R":
        return False
    return True


def check_rule(part: Dict[str, int], rule_name: str) -> str:
    """Given rule called rule_name check what happens to a given part.
    Will return R if rejected, A if accepted and a name of the next rule
    to check otherwise."""
    conditions = rules[rule_name].split(",")
    for c in conditions[:-1]:
        cond, result = c.split(":")
        var = part[cond[0]]
        val = int(cond[2:])
        passed = var > val if cond[1] == ">" else var < val
        if passed:
            return result
    return conditions[-1]


print(f"Part 1 Solution: {sum(sum(p.values()) for p in parts if part_accepted(p))}")

# stores dictionaries containing accepted combinations of ranges of values for each variable
accepted_combos: List[Dict[str, Tuple[int, int]]] = []


def find_accepted_combos(
    rules: Dict[str, str],  # See how rules is defined above
    ranges: Dict[str, Tuple[int, int]],  # See example below
    start_rule_name: str = "in",
) -> None:
    """Checks all the rules in the predefined rules dictionary and populates
    the predefind accepted_combos list. Every variable (x,m,a,s) is assumed to
    only be allowed to take values in a range defined by the ranges dictionary."""
    conditions = rules[start_rule_name].split(",")
    otherwise = conditions[-1]  # result if all conditions fail
    for c in conditions[:-1]:
        cond, result = c.split(":")
        var = cond[0]  # scoring varible to test (x,m,a,s)
        val = int(cond[2:])  # value that var must be bigger/smaller than

        if cond[1] == ">":
            pass_range = tuple([val + 1, ranges[var][1]])
            fail_range = tuple([ranges[var][0], val + 1])
        else:
            pass_range = tuple([ranges[var][0], val])
            fail_range = tuple([val, ranges[var][1]])

        ranges_pass = copy.copy(ranges)
        ranges_pass[var] = pass_range

        if result == "A":
            accepted_combos.append(ranges_pass)
        elif result != "R":
            find_accepted_combos(rules, ranges_pass, result)

        # continue checking other conditions given this one failed
        ranges[var] = fail_range

    # At this point the ranges dict has been modified to contain only the failed ranges
    if otherwise == "A":
        accepted_combos.append(ranges)
    elif otherwise != "R":
        find_accepted_combos(rules, ranges, otherwise)


ranges = {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}
find_accepted_combos(rules, ranges)
# Ranges in accepted_combos will be non overlapping hence can sum the products of all the 
# lengths of the possible ranges for each variable
print(f"Part 2 Solution: {sum(prod(x[1] - x[0] for x in rs.values()) for rs in accepted_combos)}")
