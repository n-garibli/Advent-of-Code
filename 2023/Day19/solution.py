"""Advent of Code 2023 Day 19 Solution
Completion date: 24/12/2023"""

from typing import List, Dict

with open("input_test.txt") as f:
    full_input = f.read().splitlines()
    split_i = full_input.index("")

# Store all the rules as a dictionary with their names as keys
rules: Dict[str, str] = {
    name: rule[:-1] for name, rule in [r.split("{") for r in full_input[:split_i]]
}

# Store the part infos as a list of dictionaries
parts: List[Dict[str, int]] = []
for p in full_input[split_i + 1 :]:
    scores: Dict[str, int] = {
        s1: int(s2) for s1, s2 in [s.split("=") for s in p[1:-1].split(",")]
    }
    parts.append(scores)


def part_accepted(part: Dict[str, int]) -> bool:
    """Determines whether a part is accepted given its scores"""
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


print(f"Part 1 Solution: {sum([sum(p.values()) for p in parts if part_accepted(p)])}")
