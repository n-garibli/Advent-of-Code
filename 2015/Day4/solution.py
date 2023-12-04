"""Advent of Code 2015 Day 4 Solution"""

import hashlib as h

my_input = "bgvyzdsv"

digit: int = 0
hash_pt1: int = 0
hash_pt2: int = 0

while not (hash_pt1 and hash_pt2):
    key: str = my_input + str(digit)
    key_hash: str = h.md5(key.encode()).hexdigest()
    if key_hash[:5] == "00000" and not hash_pt1:
        hash_pt1 = digit
    if key_hash[:6] == "000000" and not hash_pt2:
        hash_pt2 = digit
    digit += 1

print(f"Part 1 Solution: {hash_pt1}")
print(f"Part 2 Solution: {hash_pt2}")
