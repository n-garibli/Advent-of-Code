
''' Advent of Code 2023 Day 1 Solution '''

# Imports
import re
from typing import List, Dict

# Loading the input line by line
with open('input.txt') as f :
    lines: List[str] = [line.strip() for line in f.readlines()]


# Part 1
# -----------------------------------------------------------------------------
my_sum: int = 0
for line in lines :
    # using regex to find all digits in each line
    digits: List[str] = re.findall(r'\d', line)
    if len(digits) > 0 :
        # combining first and last digit and adding to the total sum
        my_sum += int(digits[0]+digits[-1])

print(my_sum)


# Part 2
# -----------------------------------------------------------------------------

# A useful mapping between representations of numbers 
numbers : Dict[str,int] = {'one' : '1',
                           'two' : '2',
                           'three' : '3',
                           'four' : '4',
                           'five' : '5',
                           'six' : '6',
                           'seven' : '7',
                           'eight' : '8',
                           'nine' : '9',
                           }

# Creating a horrible regex that will find all digits
regex = f'(?=('
for i,j in numbers.items() :
    regex += f"{i}|{j}|"
regex = regex[:-1] + '))'

my_sum: int = 0
for line in lines :
    digits: List[str] = re.findall(regex, line)

    if len(digits) > 0 :
        # Converting first and last items into actual digits if necessary 
        first = digits[0] if digits[0] not in numbers.keys() else numbers[digits[0]]
        last = digits[-1] if digits[-1] not in numbers.keys() else numbers[digits[-1]]
        my_sum += int(first + last)
    
print(my_sum)

