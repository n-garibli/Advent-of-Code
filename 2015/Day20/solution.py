"""Advent of Code 2015 Day 20 Solution
Completed on 31/12/2023 - optimisations needed
as both parts run in ~30 seconds."""

from typing import Set, List


def get_divisors(n: int, max_houses: int) -> Set[int]:
    """Given a house number (n) this function returns a set
    of the ids of all the elves that visited that house
    given that each elf visits a maximum of max_houses houses"""
    ds: List[int] = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n / i < max_houses:
                ds.append(i)
            if i < max_houses:
                ds.append(n / i)
    return set(ds + [n])


def find_min_house(target_presents: int, ps_per_house: int, max_houses: int) -> int:
    """Finds the minimum house number of the house that receives
    target_presents presents given that each elf delivers ps_per_house
    presents per house and visits max_houses houses."""
    n_presents: int = 0
    house_number: int = 0
    while n_presents < target_presents:
        house_number += 1
        elfs_visited: List[int] = get_divisors(house_number, max_houses=max_houses)
        n_presents: int = sum(elfs_visited) * ps_per_house
    return house_number


print(f"Part 1 Solution: {find_min_house(34000000, 10, float('inf'))}")
print(f"Part 2 Solution: {find_min_house(34000000, 11, 50)}")
