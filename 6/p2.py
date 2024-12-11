def get_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i, j)

def is_in_loop(grid, start):

    def get_next(grid, curr_pos, dir):
        if dir == "up":
            next_pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        elif dir == "right":
            next_pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        elif dir == "down":
            next_pos = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        elif dir == "left":
            next_pos = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        for np in next_pos:
            i, j = ((np[0] + curr_pos[0]), (np[1] + curr_pos[1]))

            if grid[i][j] != "#":
                if np == (-1, 0):
                    res_dir = "up"
                elif np == (0, 1):
                    res_dir = "right"
                elif np == (1, 0):
                    res_dir = "down"
                else:
                    res_dir = "left"

                return np, res_dir

    # uses slow and fast runners!!!!
    i, j = fi, fj = start
    dir = "up"
    fdir = "up"
        
    while -1 < i < len(grid) and -1 < j < len(grid[0]) and -1 < fi < len(grid) and -1 < fj < len(grid[0]):
        if dir == "up" and i == 0:
            break
        elif dir == "right" and j == len(grid[0]) - 1:
            break
        elif dir == "down" and i == len(grid) - 1:
            break
        elif dir == "left" and j == 0:
            break
        elif fdir == "up" and fi == 0:
            break
        elif fdir == "right" and fj == len(grid[0]) - 1:
            break
        elif fdir == "down" and fi == len(grid) - 1:
            break
        elif fdir == "left" and fj == 0:
            break
 
        next_pos, dir = get_next(grid, (i, j), dir)
        i, j = i + next_pos[0], j + next_pos[1]

        fnext_pos, fdir = get_next(grid, (fi, fj), fdir)
        fi, fj = fi + fnext_pos[0], fj + fnext_pos[1]
        if fdir == "up" and fi == 0:
            break
        elif fdir == "right" and fj == len(grid[0]) - 1:
            break
        elif fdir == "down" and fi == len(grid) - 1:
            break
        elif fdir == "left" and fj == 0:
            break
        fnext_pos, fdir = get_next(grid, (fi, fj), fdir)
        fi, fj = fi + fnext_pos[0], fj + fnext_pos[1]

        if (i, j) == (fi, fj) and dir == fdir:
            return 1
 
    return 0

grid = [list(l) for l in open("i1").read().splitlines()]
res = 0

start = get_start(grid)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) != start and grid[i][j] == ".":
            grid[i][j] = "#"
            res += is_in_loop(grid, start)
            grid[i][j] = "."

print(res)
