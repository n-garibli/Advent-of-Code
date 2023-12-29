"""Advent of Code 2015 Day 10 Solution
Written in Jan 2023 (with a minor Dec 2023 reformat to print solutions more neatly).
Doesn't use regex unlike the new solution so perhaps is easier to understand."""

def elf_talk(inp) :
    new_num = []
    prev_val = 0
    for i,val in enumerate(inp) :
        j = 1
        if val == prev_val :
            continue
        while i+j < len(inp)-1 :
            if inp[i+j] == val :
                j +=1
            else :
                break
        new_num.append(str(j))
        new_num.append(val)
        prev_val = val
    return ''.join(new_num)

def apply_elf_talk(num: str, n: int) -> str:
    count = 0
    while count < n :
        num = elf_talk(num)
        count += 1
    return num

print(f"Part 1 Solution: {len(apply_elf_talk('1113222113', 40))}")
print(f"Part 2 Solution: {len(apply_elf_talk('1113222113', 50))}")