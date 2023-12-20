"""Advent of Code 2015 Day 7 Solution"""

from typing import Dict, Union

with open("input_test.txt") as f:
    lines = [line.strip().split(" -> ") for line in f.readlines()]

# Dictionary which stores the wiring instructions for each wire
# The instructions will be replaced with the signal values for that wire once
# the signal has been computed - this avoids a lot of unecessary recalculations
connections: Dict[str, Union[str, int]] = {target: source for (source, target) in lines}


def get_signal(wire_id: str) -> int:
    """Returns the signal of a wire (given a wire id such as 'a') based on the
    information stored in the 'connections' dictionary defined above."""

    if wire_id.isdigit():
        # Handles cases where instructions contain numbers (eg : 1 AND wire_id)
        return int(wire_id)

    # Extract information for given wire id
    source = connections[wire_id]

    if isinstance(source, int):
        # signal for this wire has already been computed and stored
        return source
    elif source.isdigit():
        # instructions directly state what the signal for this wire is
        return int(source)
    elif "AND" in source:
        inp1, inp2 = source.split(" AND ")
        connections[wire_id] = get_signal(inp1) & get_signal(inp2)
    elif "OR" in source:
        inp1, inp2 = source.split(" OR ")
        connections[wire_id] = get_signal(inp1) | get_signal(inp2)
    elif "LSHIFT" in source:
        inp, shift = source.split(" LSHIFT ")
        connections[wire_id] = get_signal(inp) << int(shift)
    elif "RSHIFT" in source:
        inp, shift = source.split(" RSHIFT ")
        connections[wire_id] = get_signal(inp) >> int(shift)
    elif "NOT" in source:
        inp = source.split("NOT ")[-1]
        connections[wire_id] = 65535 - get_signal(inp)
    else:
        # Handles cases such as 'lx -> a' in the instructions
        return get_signal(source)

    return connections[wire_id]


# this is the part 1 solution and the wire b signal for part 2
new_b_signal: int = get_signal("a")

# resetting all the wires
connections: Dict[str, Union[str, int]] = {target: source for (source, target) in lines}
connections["b"] = new_b_signal

print(f"Part 1 Solution: {new_b_signal}")
print(f"Part 2 Solution: {get_signal('a')}")
