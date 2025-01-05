
if __name__ == "__main__":
    grid = [list(int(d) for d in l) for l in open("10/i0.txt").read().splitlines()]

    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    
    for th in trailheads:
        pass
    # do modifies DFS to find vals