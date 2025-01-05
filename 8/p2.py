from itertools import combinations

def get_points(grid, start, delta_i, delta_j):
    points = set()
    points.add(start)
    curr_i, curr_j = start

    while 0 <= curr_i + delta_i < len(grid[0]) and 0 <= curr_j + delta_j < len(grid[1]):
        curr_i += delta_i
        curr_j += delta_j
        points.add((curr_i, curr_j))

    return points

if __name__ == "__main__":
    grid = [list(l) for l in open("8/i1.txt").read().splitlines()]
    antennas = {}
    seen = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val != ".":
                if val not in antennas:
                    antennas[val] = []
                antennas[val].append((i, j))

    for freq, coords in antennas.items():
        for p1, p2 in combinations(range(len(coords)), r=2):
            p1i, p1j, p2i, p2j = coords[p1][0], coords[p1][1], coords[p2][0], coords[p2][1]
            # ensure p1 = leftmost point
            if p1j > p2j:
                p1i, p2i, p1j, p2j = p2i, p1i, p2j, p1j 

            delta_i, delta_j = p2i - p1i, p2j - p1j

            if p1i >= p2i: # pos slope
                delta_i *= -1
                slope_points = get_points(grid, (p2i, p2j), delta_i, -delta_j).union(get_points(grid, (p2i, p2j), -delta_i, delta_j))
            elif p1i < p2i: # neg slope
                slope_points = get_points(grid, (p2i, p2j), -delta_i, -delta_j).union(get_points(grid, (p2i, p2j), delta_i, delta_j))

            seen = seen.union(slope_points)            

    print(len(seen))