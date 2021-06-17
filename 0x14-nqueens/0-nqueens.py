#!/usr/bin/python3
"""
N queens problem
"""


from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = 0
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)


def validator(grid):
    """
    checks if grid is valid
    """
    checker = True
    for i in range(len(grid)):
        colSum = 0
        for j in range(len(grid)):
            colSum += grid[j][i]
        if sum(grid[i]) > 1 or colSum > 1:
            return False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                checker = checkDiag(grid, (i, j))
    return checker


def checkDiag(grid, point):
    lista = [
        (point[0]-1, point[1]-1),
        (point[0]-1, point[1]+1),
        (point[0]+1, point[1]-1),
        (point[0]+1, point[1]+1)
        ]
    corrPos = []
    l = len(grid)
    for tup in lista:
        if not (tup[0] < 0 or tup[1] < 0 or tup[0] >= l or tup[1] >= l):
            corrPos.append(tup)
    for tup in corrPos:
        if grid[tup[0]][tup[1]] == 1:
            return False
    return True


def get_solutions(size, grid, col=0, solutions=[], sol=[]):
    if col == size:
        solutions.append(sol[:])
        return solutions
    for i in range(size):
        grid[col][i] = 1
        if (validator(grid)):
            sol.append([col, i])
            get_solutions(size, grid, col+1, solutions, sol)
            sol.remove([col, i])

        grid[col][i] = 0
    return solutions


def gridMaker(size):
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[-1].append(0)
    return grid

grid = gridMaker(N)
for i in get_solutions(N, grid):
    print(i)
