"""Advent of Code 2015 Day 22 Solution
Completed on 01/01/2024. Currently part 1 runs
in 10 seconds, could be nice to add an optimisation to get a better order in 
which the possible games are checked (so the cheapest comes out first)"""

from typing import Dict, List, Optional
import copy


class Boss:
    """Class representing boss whos hits I need to drive to 0"""

    def __init__(self) -> None:
        # my puzzle input
        self.hits: int = 71
        self.damage: int = 10

    def attack(self, player) -> None:
        """Updates player and boss stats after boss' attack"""
        player.hits -= max(1, (self.damage - (7 if player.shield_counter else 0)))
        player.update(self)


class Player:
    spell_shop: Dict[str, int] = {
        "magic_missile": 53,
        "drain": 73,
        "shield": 113,
        "poison": 173,
        "recharge": 229,
    }

    def __init__(self) -> None:
        self.hits: int = 50
        self.mana: int = 500
        self.total_mana_spent: int = 0
        self.poison_counter: int = 0
        self.shield_counter: int = 0
        self.recharge_counter: int = 0

    def get_valid_spells(self) -> List[str]:
        """Returns a list of the spells the player is able to cast on their next move"""
        spells: List[str] = [
            name for name, cost in self.spell_shop.items() if cost <= self.mana
        ]
        for counter, spell in zip(
            [self.poison_counter, self.shield_counter, self.recharge_counter],
            ["poison", "shield", "recharge"],
        ):
            if counter > 1 and spell in spells:
                spells.remove(spell)
        return spells

    def update(self, boss: Boss) -> None:
        """Updates player and boss stats for the round depending on
        what effects are active"""
        if self.poison_counter:
            boss.hits -= 3
            self.poison_counter -= 1
        if self.shield_counter:
            self.shield_counter -= 1
        if self.recharge_counter:
            self.mana += 101
            self.recharge_counter -= 1

    def attack(self, boss: Boss, spell: str) -> None:
        """Updates player and boss stats after players attack with 'spell'."""
        self.mana -= self.spell_shop[spell]
        self.total_mana_spent += self.spell_shop[spell]
        self.update(boss)

        if spell == "magic_missile":
            boss.hits -= 4
        elif spell == "drain":
            boss.hits -= 2
            self.hits += 2
        elif spell == "poison":
            self.poison_counter = 6
        elif spell == "shield":
            self.shield_counter = 6
        elif spell == "recharge":
            self.recharge_counter = 5


def find_min_winning_mana(
    player: Player,
    boss: Boss,
    min_winning_mana: int,
    next_spell: Optional[str] = None,
    hard_mode: bool = False,
) -> None:
    """Returns minimum amount of mana needed for player to win against the boss (optionally given the next spell
    that the player is going to cast). If hard mode is enabled, players hits will go down by 1 at the start of every
    one of their own turns."""

    if next_spell is not None:
        if hard_mode:
            if player.hits <= 1:
                return min_winning_mana
            player.hits -= 1
        player.attack(boss, next_spell)

        if boss.hits <= 0:
            min_winning_mana = min(min_winning_mana, player.total_mana_spent)
            return min_winning_mana
        boss.attack(player)

        if boss.hits <= 0:
            min_winning_mana = min(min_winning_mana, player.total_mana_spent)
            return min_winning_mana
        if player.hits <= 0:
            return min_winning_mana

    for s in player.get_valid_spells():
        if player.total_mana_spent + player.spell_shop[s] >= min_winning_mana:
            continue
        min_winning_mana = find_min_winning_mana(
            copy.copy(player), copy.copy(boss), min_winning_mana, s, hard_mode
        )

    return min_winning_mana


print(f"Part 1 Solution: {find_min_winning_mana(Player(), Boss(), float('inf'))}")
print(f"Part 2 Solution: {find_min_winning_mana(Player(), Boss(), float('inf'), hard_mode=True)}")
