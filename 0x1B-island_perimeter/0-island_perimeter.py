#!/usr/bin/python3
"""
island perimeter python function
"""


def island_perimeter(grid):
    """
    island perimeter return perimeter
    """
    perim = 0
    length = len(grid) - 1
    width = len(grid[0]) - 1
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] != 1:
                    perim += 1
                if j == 0 or grid[i][j - 1] != 1:
                    perim += 1
                if j == width or grid[i][j + 1] != 1:
                    perim += 1
                if i == length or grid[i + 1][j] != 1:
                    perim += 1
    return perim
