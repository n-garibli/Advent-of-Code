"""Advent of Code 2023 Day 7 Solution
Completion date: 07/12/2023"""

from collections import Counter
from typing import List

with open("input_test.txt") as f:
    hands: List[str] = f.read().splitlines()


def strength(hand: str) -> int:
    """This function computes and returns the strength of each hand with
    values ranging from 0 to 6 (0 being the weakest hand, and 6 being the strongest)"""

    # number of times each unique card appears in the hand
    counts: List[int] = list(Counter(hand[:5]).values())

    # sorting means that the last element will be the maximum times an element repeats
    counts.sort()

    n_unique = len(counts)  # number of unique cards in a hand
    if n_unique == 1:  # 5 of a kind
        return 6
    elif n_unique == 2 and counts[-1] == 4:  # 4 of a kind
        return 5
    elif n_unique == 2 and counts[-1] == 3:  # full house
        return 4
    elif n_unique == 3 and counts[-1] == 3:  # 3 of a kind
        return 3
    elif n_unique == 3 and counts[-1] == 2:  # two pair
        return 2
    elif n_unique == 4:  # pair
        return 1
    else:  # high card
        return 0


def jokerize(hand: str) -> str:
    """This function replaces all the jokers in a hand
    to turn it into the best possible hand"""

    if "J" not in hand:  # no jokers to replace in the hand
        return hand

    max_strength: int = strength(hand)
    best_hand: str = hand

    for card in set(hand[:5]) - {"J"}:
        if max_strength == 6:
            # cant improve the hand any more
            break

        new_hand = hand.replace("J", card)
        new_strength = strength(new_hand)
        if new_strength > max_strength:
            max_strength = new_strength
            best_hand = new_hand

    return best_hand


cards: List[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ordered_hands: List[str] = sorted(
    hands, key=lambda x: [strength(x)] + [cards.index(x[i]) for i in range(5)]
)

print(f"Part 1 Solution: {sum([(rank+1)*int(hand[6:]) for rank,hand in enumerate(ordered_hands)])}")

cards: List[str] = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
ordered_hands: List[str] = sorted(
    hands, key=lambda x: [strength(jokerize(x))] + [cards.index(x[i]) for i in range(5)]
)

print(f"Part 2 Solution: {sum([(rank+1)*int(hand[6:]) for rank,hand in enumerate(ordered_hands)])}")
