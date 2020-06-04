# counts all the possible paths in a grid recursively
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER n, the dimensions of the grid
# 2. INTEGER row, current row
# 3. INTEGER col, current col
def count_paths(n, row, col):
    dim_adj = n-1
    curr_row = row
    curr_col = col
    if curr_row == dim_adj:
        return 1
    elif curr_col == dim_adj:
        return 1
    else:
        return count_paths(n, curr_row, curr_col+1) + count_paths(n, curr_row+1, curr_col)

# recursively gets the greatest sum of all the paths in the grid
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. 2D LIST grid, the grid itself
# 2. INTEGER n, the dimensions of the grid
# 3. INTEGER row, current row
# 4. INTEGER col, current col
def path_sum(grid, n, row, col):
    dim_adj = n-1
    curr_row = row
    curr_col = col
    if curr_row == dim_adj and curr_col != dim_adj:
        return path_sum(grid, n, curr_row, curr_col+1) + grid[curr_row][curr_col]
    elif curr_col == dim_adj and curr_row != dim_adj:
        return path_sum(grid, n, curr_row+1, curr_col) + grid[curr_row][curr_col]
    elif curr_row == dim_adj and curr_col == dim_adj:
        return grid[curr_row][curr_col]
    else:
        return max(path_sum(grid, n, curr_row, curr_col+1)+grid[curr_row][curr_col], 
        path_sum(grid, n, curr_row+1, curr_col) + grid[curr_row][curr_col])

# The function accepts following parameters:
# 1. INTEGER n, the dimensions of the grid
# 2. 2D LIST grid, the grid itself
def main():
    f = open("path.txt", "r")
    grid = []
    while True:
        line = f.readline()
        if not line: 
            del grid[-1]
            for i in grid:
                print(i)
            
            break
        else:
            line = line.split()
            int_line = []
            for i in line:
                int_line.append(int(i))
            grid.append(int_line)
    f.close()

    n = len(grid)

    print("Number of paths in a grid of dimension", n, "is", count_paths(n, 0, 0))
    print()
    print("Greatest path sum is", path_sum(grid, n, 0, 0))

if __name__ == "__main__":
    main()
