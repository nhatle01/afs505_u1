""" A Python script that implements Conway's Game of Life.
.. module:: game_of_life
   :platform:
   :synopsis: The Game of Life uses a 2-dimensional grid of cells that can
   either be in a state of “on” or “off”.This script simulates a living system
   in which cells can interact with their immediate neighbors. At the beginning
   of the simulation, some of the cells are on and some are off, and as time
   progresses the cells will change states depending on the state of their
   neighbors at each time point.
..moduleauthor:: NHAT LE <nhat.t.le@wsu.edu>

Name of the reviewr: Ricky Thai
Grade provided by the reviewer: 100

"""

import sys


def init_grid(grid, indexes):
    """ Cell indexes passed in the argument to turn ON are assigned to integer value 1.
    :param grid: a 2D list of cells.
    :type grid: array of integers that reprsent cells in grid.
    :param indexes: cell indexes.
    :type indexes: integer that stores values of passed in cell coordinates.
    """

    row = []  # store a list of row elements
    col = []  # store a list of column elements
    index = 0
    for i in indexes:  # for each elements in indexes
        # splitting the index argument into row and column elements seperately
        row_element, col_element = i.split(':')
        row.append(int(row_element))  # adding elements to the end of row list
        col.append(int(col_element))  # adding elements to the end of column list
        index = index + 1
    index = index - 1   # out of range otherwise
    while index >= 0:  # for every values in row and column
        grid[row[index]][col[index]] = 1  # replace alive cell by 1.
        index = index - 1


def make_move(grid, n, m):
    """ Plays the games and turns cell "on" or "off" when applicable.
    :param grid: a 2D list of cells.
    :type grid: array of integers that reprsent cells in grid.
    :param n: number of rows in the grid.
    :type n: integer.
    :param m: number of columns in the grid.
    :type m: integer.
    return: new grids after each time the game is played.
    """

    new_grid = [] # create a new grid to play the game.
    for i in range(n):
        new_grid.append([0]*m)

    for i in range(1, n-1):  # 1-30
        for j in range(1, m-1):  # 1-80
            center = grid[i][j]
            top = grid[i-1][j]
            top_left = grid[i-1][j-1]
            top_right = grid[i-1][j+1]
            left = grid[i][j-1]
            right = grid[i][j+1]
            bottom = grid[i+1][j]
            bottom_left = grid[i+1][j-1]
            bottom_right = grid[i+1][j+1]
            neighbor_list = [top, top_left, top_right, left, right,
                             bottom, bottom_left, bottom_right]
            sum_neighbor = sum(neighbor_list)

            new_grid[i][j] = center
            if center == 1:
                if sum_neighbor < 2 or sum_neighbor > 3:
                    new_grid[i][j] = 0
            if center == 0:
                if sum_neighbor == 3:
                    new_grid[i][j] = 1

    return new_grid


def print_grid(grid, n, m):
    """ Display the grid with "-" and "x" for off and on cells respectively.
    :param grid: a 2D list of cells.
    :type grid: array of integers that reprsent cells in grid.
    :param n: number of rows in the grid.
    :type n: integer.
    :param m: number of columns in the grid.
    :type m: integer.
    """
    display_grid = []  # new grid contains 'x' and '-', so the original grid remains 0 and 1
    for i in range(n):
        display_grid.append(['']*m)

    for i in range(1, n-1):
        for j in range(1, m-1):
                if grid[i][j] == 0:
                    display_grid[i][j] = '-'
                else:
                    display_grid[i][j] = 'x'

    for row in display_grid:
        print(''.join(row))


def main():
    """ Run the functions that are called in main.
    Main function stores the local parameters: grid, n, m and passes them into the
    functions to run the script when excecuted.
    """
    argv = sys.argv
    ticks = int(argv[1]) # store tick argument
    indexes = argv[2:] # store cell indexes passed in arguments to locate the cells.

    n = 32 # number of rows
    m = 82 # number of columns
    grid = [] # list of rows and columns

    for i in range(n):
        grid.append([0]*m)

    init_grid(grid, indexes)

    print_grid(grid, n, m)

    for i in range(ticks):
        grid = make_move(grid, n, m)
        print_grid(grid, n, m)

main()
