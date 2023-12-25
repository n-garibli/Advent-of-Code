"""Advent of Code 2022 Day 7 Solution"""

import re
from typing import List, Dict
from collections import defaultdict

with open("input_test.txt") as f:
    commands: List[str] = f.read().splitlines()

# This will contain a list of the names of the child directories for each parent directory
dir_children: Dict[str, List[str]] = defaultdict(lambda: [])

# This will contains the total sizes of the files in every directory (only files!)
dir_sizes: Dict[str, int] = defaultdict(lambda: 0)

# This will keep track of what the current directory is
current_dir = ""

for c in commands:
    if c.startswith("$ cd "):
        if c.endswith(".."):
            current_dir = "/" + "/".join(current_dir[1:-1].split("/")[:-1]) + "/"
            if current_dir == "//":
                current_dir = "/"
        else:
            current_dir += (c[5:] + "/") if c[5:] != "/" else "/"
    elif c == "$ ls":
        # Although this seems redundant for a defaultdict, this is necessary as I want
        # to access all the keys that have been explicitly added later
        dir_sizes[current_dir] = 0
        continue
    else:
        if c.startswith("dir "):
            dir_children[current_dir].append(current_dir + c[4:] + "/")
        else:
            dir_sizes[current_dir] += int(re.match(r"\d+", c).group())


def get_full_dir_size(directory: str):
    """This function computes the total size of a directory considering both the files
    in it and the files in its child directories"""
    total_file_size = dir_sizes[directory]
    for child in dir_children[directory]:
        total_file_size += get_full_dir_size(child)
    return total_file_size


total_dir_sizes = [get_full_dir_size(directory) for directory in dir_sizes.keys()]
outer = get_full_dir_size("/")

print(f"Part 1 Solution: {sum(i for i in total_dir_sizes if i < 100000)}")
print(f"Part 2 Solution: {min(i for i in total_dir_sizes if (40000000 - outer + i) > 0)}")
