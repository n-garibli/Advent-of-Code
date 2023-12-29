"""Advent of Code 2015 Day 15 Solution
Completed on 11/01/2023, reformatted on 29/12/2023.
This is not a general solution - only works for a 4 ingredient input because I was lazy
and didn't want to write a function that could partition max_teaspoons into n possible
ways. But that would be the way to make it general for when I come around"""

from typing import Optional, List


class Ingredient:
    """Class for storing the parameters of an ingredient"""

    def __init__(self, c, d, f, t, cal):
        self.capacity = c
        self.dur = d
        self.flavor = f
        self.texture = t
        self.calories = cal


# It was much quicker to manually do this than to find a general way
# to parse this input.
frosting = Ingredient(4, -2, 0, 0, 5)
candy = Ingredient(0, 5, -1, 0, 8)
butterscotch = Ingredient(-1, 0, 5, 0, 6)
sugar = Ingredient(0, 0, -2, 2, 1)

ingredients: List[Ingredient] = [frosting, candy, butterscotch, sugar]


def get_best_cookie(
    ings: List[Ingredient], max_teaspoons: int = 100, desired_cals: Optional[int] = None
) -> int:
    """Outputs the maximum cookie score by trying every possible combination of number of teaspoons for
    all the input ingredients so that the maximum total number of teaspoons is max_teaspoons. If desired_cals
    is provided, only combinations that add up to that amount of calories will be considered.
    Note: Only works for 4 ingredients."""
    assert len(ings) == 4, f"Function only optimised for 4 ingredients, got {len(ings)}"
    max_score = 0
    for f in range(max_teaspoons + 1):  # number of frosting teaspoons
        for c in range(max_teaspoons + 1 - f):  # number of candy teaspoons
            for b in range(
                max_teaspoons + 1 - f - c
            ):  # number of butterscotch teaspoons
                s = max_teaspoons - f - c - b  # number of sugar teaspoons
                calories = (
                    sum((i.calories) * j for i, j in zip(ings, [f, c, b, s]))
                    if desired_cals is not None
                    else None
                )
                if calories == desired_cals:
                    capacity = sum((i.capacity) * j for i, j in zip(ings, [f, c, b, s]))
                    durability = sum((i.dur) * j for i, j in zip(ings, [f, c, b, s]))
                    flavor = sum((i.flavor) * j for i, j in zip(ings, [f, c, b, s]))
                    texture = sum((i.texture) * j for i, j in zip(ings, [f, c, b, s]))
                    if not any(i < 0 for i in [capacity, durability, flavor, texture]):
                        # score goes to 0 if any property is negative
                        max_score = max(
                            capacity * durability * flavor * texture, max_score
                        )
    return max_score


print(f"Part 1 Solution: {get_best_cookie(ingredients, max_teaspoons=100)}")
print(f"Part 2 Solution: {get_best_cookie(ingredients, max_teaspoons=100, desired_cals=500)}")
