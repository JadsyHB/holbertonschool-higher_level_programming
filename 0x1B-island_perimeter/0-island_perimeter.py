#!/usr/bin/python3
"""
island perimeter python function
"""


def island_perimeter(grid):
    """
    island perimeter return perimeter
    """
    perim = 0
    length = len(grid)
    width = len(grid[0])
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or i == length - 1:
                    perim += 1
                if j == 0 or j == width - 1:
                    perim += 1
                if grid[i-1][j] == 0:
                    perim += 1
                if i < length-1 and grid[i+1][j] == 0:
                    perim += 1
                if grid[i][j-1] == 0:
                    perim += 1
                if j < width-1 and grid[i][j+1] == 0:
                    perim += 1
    return perim
