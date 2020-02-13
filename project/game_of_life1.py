""" A Python script that implements Conway's Game of Life.
.. module:: game_of_life
   :platform:
   :synopsis: This script simulates a living system in which cells can interact
   with their immediate neighbors. At the beginning of the simulation, some of
   the cells are on and some are off, and as time progresses the cells will
   change states depending on the state of their neighbors at each time point.
..moduleauthor:: NHAT LE <nhat.t.le@wsu.edu>

"""

import sys
def init_grid(grid,indexes):
    """
    """
    row = [] # creat a list of row elements
    col = [] # creat a list of column elements
    index = 0
    for i in indexes: # for each elements in indexes
        row_element, col_element = i.split(':') # splitting the index argument into row and column elements seperately
        row.append(int(row_element)) # adding elements to the end of row list
        col.append(int(col_element)) # adding elements to the end of column list
        index = index + 1
    index = index - 1   # out of range otherwise
    while index >= 0: # for every values in row and column
        grid[row[index]][col[index]] = 1 # replace alive cell by 1.
        index = index - 1

def make_move(grid,n,m):
    """
    """
    n = 30
    m = 80
    for i in range(n):
        for j in range(m):
            if i > 2 and j > 2:
                center = grid[i][j]
                top = grid[i-1][j]
                top_left = grid[i-1][j-1]
                top_right = grid[i-1][j+1]
                left = grid[i][j-1]
                right = grid[i][j+1]
                bottom = grid[i+1][j]
                bottom_left = grid[i+1][j-1]
                bottom_right = grid[i+1][j+1]
                neighbor_list = [top, top_left, top_right, left, right, bottom, bottom_left, bottom_right]
                sum_neighbor = sum(neighbor_list)
#                print(sum_neighbor)

                while center == 'x':
                    if sum_neighbor < 2 or sum_neighbor > 3:
                        center = '-'
                    else:
                        center = 'x'

                while center == '-':
                    if sum_neighbor == 3:
                        center = 'x'
                    else:
                        center = '-'

def print_grid(grid,n,m):
    """
    """
    for i in range(n):
        for j in range(m):
            grid[0][j] = '' # remove the (-) from row 0 and replace it with '' (blank) so the first row of the grid is row 1.
            grid[i][0] = '' # remove the (-) from column 0 and replace it with ''(blank) so the first column of the grid is column 1.
            if grid[i][j] == 0:
                grid[i][j] = '-'
            else:
                grid[i][j] = 'x'
    for row in grid:
        print(''.join(str(elem) for elem in row))

def main():
    """
    """
    argv = sys.argv
    script = argv[0]
    ticks = int(argv[1])
    indexes = argv[2:]

    n = 31
    m = 81
    grid = []

    for i in range(n):
        grid.append([0]*m)

    init_grid(grid,indexes)
    make_move(grid,n,m)
    print_grid(grid,n,m)
main()
