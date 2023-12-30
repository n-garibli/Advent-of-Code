"""This is bad code producing a solution for Advent of Code 2015 Day 18.
Written on 18/01/2023 and is only here for comparison with solution.py
Enjoy the for loops iterating through every coordinate in the array and
the code duplication to recreate the original light grid from the input 
for part 2 :)
"""

# Imports and Loading Input
import numpy as np

with open('input.txt') as f :
    my_list = [line.strip() for line in f.readlines()]

# Creating array of lights

grid = np.zeros((len(my_list),len(my_list[0])))
for i in range(len(my_list)) :
    for j in range(len(my_list[0])) :
        if my_list[i][j] == '#' : grid[i][j] = 1
dirs = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
d = len(grid)

def one_step(grid) :
    new_grid = np.zeros((d,d))
    for i in range(d) :
        for j in range(d) :
            neighbor_on = [grid[i+di[0]][j+di[1]] for di in dirs if (i+di[0] > -1 and i+di[0] < d and j+di[1] > -1 and j+di[1] < d)]
            n = neighbor_on.count(1)

            if grid[i][j] == 1 :
                if n not in [2,3] :
                    new_grid[i][j] = 0
                else : new_grid[i][j] = 1
            else :
                if n == 3 :
                    new_grid[i][j] = 1
                else : new_grid[i][j] = 0
            
    return new_grid


# Part 1

steps = 100
while steps > 0 : 
    grid = one_step(grid)
    steps += -1
print(f"Part 1 Solution: {sum(sum(grid))}")

# Part 2

grid = np.zeros((len(my_list),len(my_list[0])))
for i in range(len(my_list)) :
    for j in range(len(my_list[0])) :
        if my_list[i][j] == '#' : grid[i][j] = 1
grid[0][0] = 1
grid[d-1][d-1] = 1
grid[0][d-1] = 1
grid[d-1][0] = 1

steps = 100
while steps > 0 : 
    grid = one_step(grid)
    grid[0][0] = 1
    grid[d-1][d-1] = 1
    grid[0][d-1] = 1
    grid[d-1][0] = 1
    steps += -1
print(f"Part 2 Solution: {sum(sum(grid))}")
