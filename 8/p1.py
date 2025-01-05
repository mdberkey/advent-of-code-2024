from itertools import combinations

if __name__ == "__main__":
    grid = [list(l) for l in open("8/i1.txt").read().splitlines()]
    antennas = {}
    seen = {}

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
                node1, node2 = (p1i + delta_i, p1j - delta_j), (p2i - delta_i, p2j + delta_j)
            elif p1i < p2i: # neg slope
                node1, node2 = (p1i - delta_i, p1j - delta_j), (p2i + delta_i, p2j + delta_j)

            if 0 <= node1[0] < len(grid) and 0 <= node1[1] < len(grid[0]): 
                if node1 not in seen:
                    seen[node1] = 0
                seen[node1] += 1
            if 0 <= node2[0] < len(grid) and 0 <= node2[1] < len(grid[0]):
                if node2 not in seen:
                    seen[node2] = 0
                seen[node2] += 1
            
    print(len(seen))