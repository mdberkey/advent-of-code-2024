def get_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i, j)

def get_num_seen(grid, start):

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
    
    seen = set()
    i, j = start
    dir = "up"
        
    while -1 < i < len(grid) and -1 < j < len(grid[0]):
        if (i, j) not in seen:
            seen.add((i, j))
        
        if dir == "up" and i == 0:
            break
        elif dir == "right" and j == len(grid[0]) - 1:
            break
        elif dir == "down" and i == len(grid) - 1:
            break
        elif dir == "left" and j == 0:
            break
 
        next_pos, dir = get_next(grid, (i, j), dir)
        i, j = i + next_pos[0], j + next_pos[1]    
    
    return len(seen)

grid = [list(l) for l in open("i1").read().splitlines()]
res = 0

start = get_start(grid)
res = get_num_seen(grid, start)

print(res)
