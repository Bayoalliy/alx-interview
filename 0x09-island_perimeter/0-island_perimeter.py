#!/usr/bin/python3
"""
calculating the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of island"""
    lst = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                lst.append(grid[i - 1][j])
                lst.append(grid[i + 1][j])
                lst.append(grid[i][j - 1])
                lst.append(grid[i][j + 1])
    return(len([i for i in lst if i == 0]))
