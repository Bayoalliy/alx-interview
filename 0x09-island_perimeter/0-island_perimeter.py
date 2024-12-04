#!/usr/bin/python3
"""
calculating the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of island"""
    if type(grid) != list:
        return 0

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
