"""Advent of Code 2015 Day 11 Solution
Completed in Jan 2023, rewritten on 29/12/2023 with 
reformat and a speed optimisation"""

from string import ascii_lowercase as lc
from typing import List

cond1_test: List[str] = [lc[i] + lc[i + 1] + lc[i + 2] for i in range(len(lc) - 2)]
cond3_test: List[str] = [i + i for i in lc]  # all double letters (aa,bb,etc)


def get_new_password(old_password: str) -> str:
    """Returns santas next valid password based on the old password"""

    p_word = old_password
    for i in ["i", "o", "l"]:
        # speed up in case old password contains forbidden letters
        if i in p_word:
            val_update = lc[lc.index(i) + 1]
            j = p_word.index(i)
            p_word = p_word[:j] + val_update + "a" * (len(p_word) - j)
    while True:
        # one incremental password update
        for i, val in enumerate(p_word[::-1]):
            if val != "z":
                idx = lc.index(val)
                val_update = lc[idx + 1] if val not in ["h", "n", "k"] else lc[idx + 2]
                p_word = p_word[: -(i + 1)] + val_update + "a" * i
                break

        if (
            any(i in p_word for i in cond1_test)
            and sum(i in p_word for i in cond3_test) > 1
        ):
            # return the first password to pass all conditions
            # no need to check second condition as it is accounted for
            return p_word


new_password = get_new_password("hxbxwxba")
print(f"Part 1 Solution: {new_password}")
print(f"Part 2 Solution: {get_new_password(new_password)}")
