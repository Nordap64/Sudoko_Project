grid = [[0, 5, 0, 0, 0, 8, 0, 0, 4],
        [0, 0, 2, 0, 0, 9, 1, 6, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 6, 0, 0, 0, 9, 0, 0],
        [0, 0, 8, 7, 0, 6, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 4, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 7, 3, 8, 0, 0, 6, 0, 0],
        [1, 0, 0, 2, 0, 0, 0, 7, 0]]


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if try_num(x, y, num):
                        grid[y][x] = num
                        solve()
                        grid[y][x] = 0
                return
    print_grid()


def try_num(x, y, num):
    global grid
    if grid[y].__contains__(num):
        return False
    for i in range(9):
        if grid[i][x] == num:
            return False
    xGrid = (x//3) * 3
    yGrid = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[yGrid + i][xGrid + j] == num:
                return False
    return True


def print_grid():
    for y in range(9):
        print(grid[y])
    print("\n")
    return


print_grid()
solve()
