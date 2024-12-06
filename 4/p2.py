grid= [list(l) for l in open("i1").read().splitlines()]

XMAS = ["X", "M", "A", "S"]
res = 0

def check_val(i, j, grid, max_i, max_j):
    count = 0
    if grid[i][j] != "A":
        return 0

    if j < max_j - 1 and i < max_i - 1 and j >= 1 and i >= 1:
        if grid[i-1][j-1] == "M" and grid[i-1][j+1] == "M":
            if grid[i+1][j-1] == "S" and grid[i+1][j+1] == "S":
                count += 1
        elif grid[i-1][j+1] == "M" and grid[i+1][j+1] == "M":
            if grid[i-1][j-1] == "S" and grid[i+1][j-1] == "S":
                count += 1
        elif grid[i+1][j-1] == "M" and grid[i+1][j+1] == "M":
            if grid[i-1][j-1] == "S" and grid[i-1][j+1] == "S":
                count += 1
        elif grid[i-1][j+1] == "S" and grid[i+1][j+1] == "S":
            if grid[i-1][j-1] == "M" and grid[i+1][j-1] == "M":
                count += 1
    return count

for i in range(len(grid)):
    for j in range(len(grid[0])):
        res += check_val(i, j, grid, len(grid), len(grid[0]))

print(res)
