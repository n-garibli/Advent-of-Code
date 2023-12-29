"""Advent of Code 2015 Day 10 Solution
Completed in 2022 (see old_solution.py), rewritten on 29/12/2023 
to use regex for a shorter solution"""

import re


def apply_elf_talk(num: str, n: int) -> str:
    """This function transforms the input number (num) into elf talk n times
    and returns the transformed number"""
    for _ in range(n):
        num = "".join([str(len(rep)) + val for rep, val in re.findall(r"((\d)\2*)", num)])
    return num


num_after_40 = apply_elf_talk("1113222113", 40)
print(f"Part 1 Solution: {len(num_after_40)}")
# apply elf talk 10 more times to get 50 total iterations
print(f"Part 2 Solution: {len(apply_elf_talk(num_after_40, 10))}")
