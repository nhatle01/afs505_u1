import sys

argv = sys.argv
script = argv[0]
ticks = int(argv[1])
indexes = argv[2:]

row = [] # creat a list of row elements
col = [] # creat a list of column elements

index = 0

for i in indexes: # for each elements in indexes
    row_col = i
    row_element, col_element = row_col.split(':') # splitting the index argument into row and column elements seperately
    row.append(int(row_element)) # adding elements to the end of row list
    col.append(int(col_element)) # adding elements to the end of column list
    #print(row[index], end = ' ')
    #print(col[index])
    #print(index)
    index = index + 1

n = 31
m = 81
a = [] # create an empty grid to store values in.
b = []
for i in range(n):
    a.append(['-']*m) # create the grid of [81 * (-)] in one row with 31 rows in total.

for i in range(n):
    b.append(['-']*m) # create the grid of [81 * (-)] in one row with 31 rows in total.


index = index - 1   # out of range otherwise
neightbor_index = index
for i in range(n):
    for j in range(m):
        a[0][j] = '' # remove the (-) from row 0 and replace it with '' (blank) so the first row of the grid is row 1.
        a[i][0] = '' # remove the (-) from column 0 and replace it with ''(blank) so the first column of the grid is column 1.
        b[0][j] = '' # remove the (-) from row 0 and replace it with '' (blank) so the first row of the grid is row 1.
        b[i][0] = '' # remove the (-) from column 0 and replace it with ''(blank) so the first column of the grid is column 1.
        while index >= 0: # for every values in row and column
            a[row[index]][col[index]] = 'x' # print 'x' on the grid
            b[row[index]][col[index]] = 'x' # print 'x' on the grid
            index = index - 1 # row[index] and col[index] start with elements 0 while index counts the total elements in the list.

# index out of range > 80 or > 30
n = 30
m = 80
for i in range(n):
    for j in range(m):
        if i > 2 and j > 2:
            x = i
            y = j
            #print("{},{}".format(x, y))
            top_x = i - 1
            top_y = j
            top_left_x = top_x
            top_left_y = top_y - 1
            top_right_x = top_x
            top_right_y = top_y + 1
            left_x = i
            left_y = j - 1
            right_x = i
            right_y = j + 1
            bottom_x = i + 1
            bottom_y = j
            bottom_left_x = bottom_x
            bottom_left_y = bottom_y -1
            bottom_right_x = bottom_x
            bottom_right_y = bottom_y + 1

            center = a[x][y]
            top = a[top_x][top_y]
            top_left = a[top_left_x][top_left_y]
            top_right = a[top_right_x][top_right_y]
            left = a[left_x][left_y]
            right = a[right_x][right_y]
            bottom = a[bottom_x][bottom_y]
            bottom_left = a[bottom_left_x][bottom_left_y]
            bottom_right = a[bottom_right_x][bottom_right_y]
            neighbor_list = [top, top_left, top_right, left, right, bottom, bottom_left, bottom_right]

            dead = 0
            alive = 0

            for n in neighbor_list:
                if n == '-':
                    dead = dead + 1
                else:
                    alive = alive + 1

            if center == 'x':   # living cell
                if alive < 2 or alive > 3:
                    b[x][y] = '-'  # turn off
            else:               # dead cell
                if alive == 3:
                    b[x][y] = 'x'  # turn on

tick = 0
while tick < ticks:
    for row in b:
            print(''.join(elem for elem in row))
    tick = tick + 1
