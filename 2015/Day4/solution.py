"""Advent of Code 2015 Day 4 Solution
Competion Date: 04/12/2013"""

import hashlib as h

input_ = "abcdef"

digit: int = 0
hash1: int = 0
hash2: int = 0

while not (hash1 and hash2):
    key: str = input_ + str(digit)
    key_hash: str = h.md5(key.encode()).hexdigest()
    if key_hash[:5] == "00000" and not hash1:
        hash1 = digit
    if key_hash[:6] == "000000" and not hash2:
        hash2 = digit
    digit += 1

print(f"Part 1 Solution: {hash1}")
print(f"Part 2 Solution: {hash2}")
