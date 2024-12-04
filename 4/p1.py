lines = open("input").read().splitlines()
grid= [list(l) for l in open("input").read().splitlines()]

XMAS = ["X", "M", "A", "S"]
res = 0

# not proud of this lol
def check_val(i, j, grid, max_i, max_j):
    count = 0
    if grid[i][j] != "X":
        return 0

    if j < max_j - 3:
        if grid[i][j:j+4] == XMAS:
            count += 1
    if j >= 3:
        if grid[i][j-3:j+1] == XMAS[::-1]:
            count += 1
    if i < max_i - 3:
        if grid[i+1][j] == "M" and grid[i+2][j] == "A" and grid[i+3][j] == "S":
            count += 1
    if i >= 3:
        if grid[i-1][j] == "M" and grid[i-2][j] == "A" and grid[i-3][j] == "S":
            count += 1
    if j < max_j - 3 and i < max_i - 3: # right down
        if grid[i+1][j+1] == "M" and grid[i+2][j+2] == "A" and grid[i+3][j+3] == "S":
            count += 1
    if j < max_j - 3 and i >= 3: # left down
        if grid[i-1][j+1] == "M" and grid[i-2][j+2] == "A" and grid[i-3][j+3] == "S":
            count += 1
    if j >= 3 and i >= 3: # left up
        if grid[i-1][j-1] == "M" and grid[i-2][j-2] == "A" and grid[i-3][j-3] == "S":
            count += 1
    if j >= 3 and i < max_i - 3: # right up
        if grid[i+1][j-1] == "M" and grid[i+2][j-2] == "A" and grid[i+3][j-3] == "S":
            count += 1
    
    return count

for i in range(len(grid)):
    for j in range(len(grid[0])):
        res += check_val(i, j, grid, len(grid), len(grid[0]))

print(res)
