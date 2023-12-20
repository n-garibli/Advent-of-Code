"""Advent of Code 2023 Day 4 Solution"""

from typing import List, Dict
from collections import defaultdict
import re

with open("input_test.txt") as f:
    # parsing the input line by line
    cards: List[str] = [line.strip() for line in f.readlines()]

total_points: int = 0

# stores the number of card copies for each card id with the default being 1
n_cards: Dict[int, int] = defaultdict(lambda: 1)
max_card_id: int = len(cards)

for i, card in enumerate(cards):
    card_id = i + 1
    # use regex to find all digits
    winning_numbers = re.findall(r"\d+", card.split(":")[1].split("|")[0])
    our_numbers = re.findall(r"\d+", card.split(":")[1].split("|")[1])
    n_matches = len([x for x in our_numbers if x in winning_numbers])

    # This solves the part 1 problem
    card_points = 2 ** (n_matches - 1) if n_matches > 0 else 0
    total_points += card_points

    # This solves the part 2 problem
    for j in range(1, n_matches + 1):
        if card_id + j > max_card_id:
            # no need to compute copies of cards that dont exist
            break
        # creates a copy of the card_id+jth card for each copy of current card
        n_cards[card_id + j] += 1 * n_cards[card_id]

print(f"Part 1 Solution: {total_points}")
print(f"Part 2 Solution: {sum(n_cards.values())}")
