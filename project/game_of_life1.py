from sys import argv

def init_grid(grid):
    print(grid)

def make_move(grid):
    pass

def print_grid(grid):
   for row in grid:
        print(''.join(str(elem) for elem in grid))


def main():
    n = 30
    m = 80
    a = []
    for i in range(n):
        a.append([0]*m)
    init_grid(a)
    print_grid(a)
main()
