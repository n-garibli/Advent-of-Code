"""Advent of Code 2022 Day 11 Solution
Completed in 2022, reformatted on 25/12/2023"""

from typing import List, Dict, Any, Union
import re
from math import prod

with open("input_test.txt") as f:
    # All information split by monkeys
    instructions: List[str] = f.read().split("\n\n")


def parse_input(instructions: List[str]) -> Dict[int, Dict[str, Any]]:
    """Transforms the input into a more useful format - a dictionary
    with keys corresponding to the number of each monkey containing
    a dictionary with information about how that monkey behaves. Each
    subdictionary contains the following :
        'items' : list of worry levels for items monkey currently has
        'operation' : the decription of what happens to worry level
        'test' : a number corresponding to what the divisibility check will be
        True : monkey id to pass items to if test passes
        False : monkey id to pass items to if test fails"""
    all_monkey_info: Dict[int, Dict[str, Any]] = {}

    for i, monkey in enumerate(instructions):
        monkey_info: Dict[Union[str, bool], Any] = {}
        info = monkey.split("\n")
        monkey_info["items"]: List[int] = list(map(int, re.findall(r"\d+", info[1])))
        monkey_info["operation"]: str = info[2].split("=")[-1]
        for key, j in zip(["test", True, False], [3, 4, 5]):
            monkey_info[key]: int = int(re.findall(r"\d+", info[j])[0])
        monkey_info["n_inspections"] = 0
        all_monkey_info[i] = monkey_info
    return all_monkey_info


def get_multiple(all_monkey_info: Dict[int, Dict[str, Any]]) -> int:
    """Returns the product of all numbers that are used to test divisibility"""
    return prod([monkey_info["test"] for monkey_info in all_monkey_info.values()])


def one_round(
    all_monkey_info: Dict[int, Dict[str, Any]], multiple: int, worry_decrease: bool
) -> Dict[int, Dict[str, Any]]:
    """Evolves the all_monkey_info dictionary for one round so that the items
    move around based on the behaviour of each monkey as described in the input"""
    for _, info in all_monkey_info.items():
        info["n_inspections"] += len(info["items"])
        for item in info["items"]:
            # There are only 3 types operations in the input (old*old,old+x,old*x)
            # which is why the following works
            operation_nums = re.findall(r"\d+", info["operation"])
            if len(operation_nums) == 0:
                new = item * item
            elif "*" in info["operation"]:
                new = item * int(operation_nums[0])
            else:
                new = item + int(operation_nums[0])

            if worry_decrease:
                new = new // 3

            new_monkey_id = info[new % info["test"] == 0]

            # dividing by the "multiple" is a way to keep the worry level
            # numbers low whilst not affecting the results of further test
            # as per the Chinese remainder theorem
            all_monkey_info[new_monkey_id]["items"].append(new % multiple)
        info["items"] = []
    return all_monkey_info


def get_monkey_business(
    instructions: List[str], n_rounds: int, worry_decrease: bool
) -> int:
    """Parses input and evolves the state for n_rounds rounds. If worry_decrease is
    set to True the worry levels will be divided by 3 for each item after inspection"""
    monkey_info = parse_input(instructions)
    for _ in range(n_rounds):
        monkey_info = one_round(
            monkey_info,
            worry_decrease=worry_decrease,
            multiple=get_multiple(monkey_info),
        )

    inspections = [x["n_inspections"] for x in monkey_info.values()]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


print(f"Part 1 Solution: {get_monkey_business(instructions,n_rounds=20, worry_decrease=True)}")
print(f"Part 2 Solution: {get_monkey_business(instructions,n_rounds=10000,worry_decrease=False)}")
