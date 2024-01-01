"""Advent of Code 2015 Day 23 Solution
Completed on 01/01/2024"""

from typing import List, Dict

with open("input.txt") as f:
    instructions: List[str] = f.read().splitlines()


def exec_instructions(program: List[str], registers: Dict[str, int]) -> Dict[str, int]:
    """Updates the registers using the istructions provided"""
    i = 0
    while True:
        command = program[i]
        if command.startswith("hlf"):
            registers[command[4]] = registers[command[4]] / 2
            i += 1
        elif command.startswith("tpl"):
            registers[command[4]] *= 3
            i += 1
        elif command.startswith("inc"):
            registers[command[4]] += 1
            i += 1
        elif command.startswith("jmp"):
            i += int(command[3:])
        elif command.startswith("jie"):
            i += int(command.split(",")[1]) if registers[command[4]] % 2 == 0 else 1
        elif command.startswith("jio"):
            i += int(command.split(",")[1]) if registers[command[4]] == 1 else 1
        if i >= len(program):
            break
    return registers


print(f"Part 1 Solution: {exec_instructions(instructions, {'a':0, 'b':0})['b']}")
print(f"Part 2 Solution: {exec_instructions(instructions, {'a':1, 'b':0})['b']}")
